# from behave import *
# from pages.ios.Member_Availability_Page import Availability
#
# @when(u'I see the "{department}" option displays under the Availability title')
# def title_under_availability_section(context, department):
#     context.availabilityTab = Availability(context.driver)
#     context.availabilityTab.validate_title_on_avalabilitytab(department)
#
#
# @then(u'I click on the Group Selector in the top right hand corner to view my assigned Groups')
# def view_my_assigned_groups(context):
#     context.availabilityTab = Availability(context.driver)
#     context.availabilityTab.click_on_groups_icon()
#     context.availabilityTab.view_my_groups()
#
#
# @then(u'I click on "{department}" that assigned to me from the list')
# def select_my_grp(context, department):
#     context.availabilityTab = Availability(context.driver)
#     context.availabilityTab.select_my_group(department)
#
#
# @then(u'I can choose my availibility from the Top Nav Bar: SET')
# def my_availability(context):
#     context.availabilityTab = Availability(context.driver)
#     context.availabilityTab.select_availability_day_status_from_SET()
#     context.availabilityTab.select_availability_time_from_SET()
#     context.availabilityTab.save_availability_from_SET()
#     context.availabilityTab.select_availability_from_WEEKLY()
