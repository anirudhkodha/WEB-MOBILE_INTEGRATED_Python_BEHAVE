from behave import given, when, then
from pages.web.Member_Web_page import Web_Event

@given(u'I tap on the Event Feeds')
def tap_create_broacast(context):
	web_event =  Web_Event(context.Browserdriver)
	web_event.check_and_click_on_Feeds()
@when(u'I tap the Generate report web')
def download_report(context):

	web_event = Web_Event(context.Browserdriver)
	web_event.tap_on_generate_report()

@then(u'report should be created on web to check the details')
def step_impl(context):
	web_event = Web_Event(context.Browserdriver)

@given(u'I tap on the Create Event')
def tap_on_new_broadcast(context):
	(u'STEP: Given I tap on the Create Event')



@when(u'I enter the event details on web')
def broadcast_application(context):
	web_event = Web_Event(context.Browserdriver)
	web_event.Create_event_tapon()
	web_event.Enter_event_details()


@then(u'Event should be created on web')
def step_impl(context):
	pass

#
# @then(u'event should be created on mobile')
# def step_impl(context):
# 	pass