# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sync_dokumen"
app_title = "Sync Dokumen"
app_publisher = "DAS"
app_description = "Sync Dokumen"
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = " "
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sync_dokumen/css/sync_dokumen.css"
# app_include_js = "/assets/sync_dokumen/js/sync_dokumen.js"

# include js, css files in header of web template
# web_include_css = "/assets/sync_dokumen/css/sync_dokumen.css"
# web_include_js = "/assets/sync_dokumen/js/sync_dokumen.js"

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
# get_website_user_home_page = "sync_dokumen.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sync_dokumen.install.before_install"
# after_install = "sync_dokumen.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sync_dokumen.notifications.get_notification_config"

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

doc_events = {
	"Purchase Order": {
		"on_submit": "sync_dokumen.sync_method.enqueue_sync_document_inv",
	},
	"Sync Form":{
		"on_update":"sync_dokumen.sync_method.enqueue_check_form"
	},
	"Purchase Receipt": {
		"on_submit": "sync_dokumen.sync_method.sync_received_qty",
		"on_cancel": "sync_dokumen.sync_method.cancel_sync_received_qty"
	},
	
 }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sync_dokumen.tasks.all"
# 	],
# 	"daily": [
# 		"sync_dokumen.tasks.daily"
# 	],
# 	"hourly": [
# 		"sync_dokumen.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sync_dokumen.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sync_dokumen.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sync_dokumen.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sync_dokumen.event.get_events"
# }

