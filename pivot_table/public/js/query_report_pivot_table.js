frappe.views.QueryReport = frappe.views.QueryReport.extend({

    make: function () {
        this._super();
        this.wrapper.find(".chart-area")
            .after('<div class="pivot-area"></div>')
        this.pivot_area = this.wrapper.find(".pivot-area")
    },

    make_toolbar: function () {
        var me = this;
        this._super();
        this.pivot_icon = this.page.add_action_icon("fa fa-cube", function () {
            me.pivot_area.toggle();
        });
    },

    render: function (res) {
        this._super(res);
        this.setup_pivot(res);
    },

    setup_pivot: function (res) {
        this.pivot_area.toggle(false);
        $(this.pivot_area).css("margin-top", "20px");
        $(this.pivot_area).css("margin-bottom", "20px");

        var pivot_columns = [];
        $.each(this.columns, function (i, col) { if (i > 0) pivot_columns.push(col.label); });
        res.result.unshift(pivot_columns);

        $(this.pivot_area).pivotUI(res.result, { rows: pivot_columns.slice(0, 1), columns: pivot_columns.slice(1) });
    }

})
