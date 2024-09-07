app_name = "craftinteractive"
app_title = "craftinteractive"
app_publisher = "craftinteractive"
app_description = "craftinteractive"
app_email = "craftinteractive@gmail.com"
app_license = "mit"
required_apps = ["frappe/hrms"]

# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/craftinteractive/css/craftinteractive.css"
# app_include_js = "/assets/craftinteractive/js/craftinteractive.js"

# include js, css files in header of web template
# web_include_css = "/assets/craftinteractive/css/craftinteractive.css"
# web_include_js = "/assets/craftinteractive/js/craftinteractive.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "craftinteractive/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Appraisal Cycle" : "public/js/appraisal_cycle.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "craftinteractive/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "craftinteractive.utils.jinja_methods",
# 	"filters": "craftinteractive.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "craftinteractive.install.before_install"
# after_install = "craftinteractive.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "craftinteractive.uninstall.before_uninstall"
# after_uninstall = "craftinteractive.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "craftinteractive.utils.before_app_install"
# after_app_install = "craftinteractive.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "craftinteractive.utils.before_app_uninstall"
# after_app_uninstall = "craftinteractive.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "craftinteractive.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Appraisal Cycle": "craftinteractive.craftinteractive.doctype.party.party.AppraisalCycle",
	# "Appraisal Cycle": "craftinteractive.overrides.party.set_employees"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"craftinteractive.tasks.all"
# 	],
# 	"daily": [
# 		"craftinteractive.tasks.daily"
# 	],
# 	"hourly": [
# 		"craftinteractive.tasks.hourly"
# 	],
# 	"weekly": [
# 		"craftinteractive.tasks.weekly"
# 	],
# 	"monthly": [
# 		"craftinteractive.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "craftinteractive.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "craftinteractive.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "craftinteractive.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["craftinteractive.utils.before_request"]
# after_request = ["craftinteractive.utils.after_request"]

# Job Events
# ----------
# before_job = ["craftinteractive.utils.before_job"]
# after_job = ["craftinteractive.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"craftinteractive.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

