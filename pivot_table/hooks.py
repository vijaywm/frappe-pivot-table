# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pivot_table"
app_title = "Pivot Table"
app_publisher = "vijaywm"
app_description = "Pivot Tables using PivotTable.js"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vijay_wm@yahoo.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pivot_table/css/pivot_table.css"
app_include_css = "/assets/pivot_table/js/lib/pivottable/pivot.min.css"
# app_include_js = "/assets/pivot_table/js/pivot_table.js"
app_include_js = [
    "/assets/pivot_table/js/lib/pivottable/pivot.min.js",
    "/assets/pivot_table/js/lib/jquery-ui.min.js",
    "assets/pivot_table/js/query_report_pivot_table.js"
]

# include js, css files in header of web template
# web_include_css = "/assets/pivot_table/css/pivot_table.css"
# web_include_js = "/assets/pivot_table/js/pivot_table.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pivot_table.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pivot_table.install.before_install"
# after_install = "pivot_table.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pivot_table.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pivot_table.tasks.all"
# 	],
# 	"daily": [
# 		"pivot_table.tasks.daily"
# 	],
# 	"hourly": [
# 		"pivot_table.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pivot_table.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pivot_table.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pivot_table.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pivot_table.event.get_events"
# }
