from behave import *
import time
from pages.ios.Member_Event_page import Event_Details
from pages.ios.Member_Login_Navigation_page import Login_feature


@given('I login to rfs activ with "{username}" and "{password}"')
def login_to_activ(context, username, password):
	time.sleep(2)
	retry_num = 0
	context.loginPageRfs = Login_feature(context.driver)
	context.loginPageRfs.click_login()
	print(context.driver.current_context)
	context.loginPageRfs.login(username, password)

#******************************************************************************************
# @given('I can see Group Member contacts on as Activ user')
# def activ_page_details(context):
#     pass
#     # context.loginPageRfs = Login_feature(context.driver)
#     # context.loginPageRfs.click_on_menu_icon()
#     # context.loginPageRfs.click_on_menu_icon()
#     # context.loginPageRfs.click_on_menu_contacts()
#     # context.loginPageRfs.search_contact()


# @then('I verify the contact details for the Member')
# def verify_contact_details(context):
#     pass
#     # context.loginPageRfs = Login_feature(context.driver)
#     # context.loginPageRfs.click_on_contact()
#     #
#     # context.loginPageRfs = Login_feature(context.driver)
#     # # loginPageRfs.verify_contact_details()
#     # context.driver.back()

# **************************************************************************************


@given('I click on QuickView')
def inside_quickview(context):
	time.sleep(2)
	context.loginPageRfs = Login_feature(context.driver)
	context.loginPageRfs.click_on_quickview()

@given('I click on ListView')
def inside_listview(context):
	time.sleep(2)
	context.loginPageRfs = Login_feature(context.driver)
	context.loginPageRfs.click_on_listview()



@then('I logout as a member')
def logout(context):
	context.loginPageRfs = Login_feature(context.driver)
	context.loginPageRfs.click_on_menu_icon()
	# click on settings
	context.loginPageRfs = Login_feature(context.driver)
	context.loginPageRfs.click_on_settings()
	# logout
	context.loginPageRfs = Login_feature(context.driver)
	time.sleep(4)
	context.loginPageRfs.click_on_logout()

@step(u'I am on the "{bottom_nav}" Tab from any LayoutView')
def tap_on_tab(context, bottom_nav):
	if bottom_nav=="Broadcast":
		context.eventTab = Event_Details(context.driver)
		context.eventTab.tap_on_broadcast_navigation(bottom_nav)
	if bottom_nav == "Event":
		context.eventTab = Event_Details(context.driver)
		context.eventTab.tap_on_event_navigation(bottom_nav)

# @given('I am on the "Event" Tab from Quickview')
# def tap_on_tab(context):
# 	context.eventTab = Event_Details(context.driver)
# 	context.eventTab.c()