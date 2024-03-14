# import time
from behave import *
from pages.android.Member_Broadcast_page import Broadcast



@given(u'I am on the "Broadcast" Tab for any LayoutView')
def bottom_nav(context):
	context.broadcastTab = Broadcast(context.driver)
	context.broadcastTab.click_on_broadcast_navigation()

@when(u'the member broadcast an Alert')
def broadcast_alert_creation(context):
	context.broadcastTab = Broadcast(context.driver)
	context.broadcastTab.plus_button_broadCast()
	context.broadcastTab.broadcast_alert()


@then(u'the Alert is displayed and Necessary actions can be taken')

def broadcast_alert_displayed(context):
	context.broadcastTab = Broadcast(context.driver)
	context.broadcastTab.broadcast_alert_component()
	context.broadcastTab.broadcast_alert_accept()
	context.broadcastTab.broadcast_attendance_details()
	context.broadcastTab.broadcast_alert_map()
