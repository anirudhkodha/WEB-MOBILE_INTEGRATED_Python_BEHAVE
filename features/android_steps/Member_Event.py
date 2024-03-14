# from behave import *
#
# from pages.ios.Member_Event_page import Event_Details
#
#
# @when(u'I can tap on the plus button on top right corner to create an event')
# def add_event_button(context):
# 	context.eventTab = Event_Details(context.driver)
# 	context.eventTab.click_add_event()
#
# @then(u'I can fill the necerssary options to create an event and Assert it')
# def add_event_steps(context):
# 	context.eventTab = Event_Details(context.driver)
# 	# context.eventTab.create_event_initial_steps()
# 	context.eventTab.Event_date_time_picker()
# 	# context.eventTab.create_event_last_steps()
#
#
# @then(u'I check and Assign')
# def check_assign(context):
# 	context.eventTab = Event_Details(context.driver)
# 	context.eventTab.check_for_event_component()
# 	context.eventTab.accept_event()
# 	context.eventTab.check_attendance_details()
