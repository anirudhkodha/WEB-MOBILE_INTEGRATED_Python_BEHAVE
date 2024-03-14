# import time
from behave import *
from pages.web.Member_Login_Navigation_page import Login_feature
from builtins import *



@given('I login to rfs activ with "{username}" and "{password}"')
def login_to_activ_web(context, username, password):

	loginPageRfsWeb = Login_feature(context.Browserdriver)
	loginPageRfsWeb.click_login()
	loginPageRfsWeb.login(username,password)

@given('I login to rfs activ as a member')
def login_activ_member_web(self):
	pass





# @given('I can see Group Member contacts on as Activ user')
# def activ_page_details(context):
#     context.loginPageRfs = Login_feature(context.driver)
#     context.loginPageRfs.click_on_menu_icon()
#     context.loginPageRfs.click_on_menu_icon()
#     context.loginPageRfs.click_on_menu_contacts()
#     context.loginPageRfs.search_contact()
#
#
# @then('I verify the contact details for the Member')
# def verify_contact_details(context):
#     context.loginPageRfs = Login_feature(context.driver)
#     context.loginPageRfs.click_on_contact()
#
#     context.loginPageRfs = Login_feature(context.driver)
#     # loginPageRfs.verify_contact_details()
#     context.driver.back()
#
#
# @given('I click on QuickView')
# def inside_quickview(context):
#     time.sleep(5)
#     context.loginPageRfs = Login_feature(context.driver)
#     context.loginPageRfs.click_on_quickview()
#
#
# @given('I click on ListView')
# def inside_listview(context):
#     context.loginPageRfs = Login_feature(context.driver)
#     context.loginPageRfs.click_on_listview()
#
#
@then('I logout as a member')
def logout(context):
	pass
#     context.loginPageRfs = Login_feature(context.driver)
#     context.loginPageRfs.click_on_menu_icon()
#     # click on settings
#     context.loginPageRfs = Login_feature(context.driver)
#     context.loginPageRfs.click_on_settings()
#     # logout
#     context.loginPageRfs = Login_feature(context.driver)
#     time.sleep(4)
#     context.loginPageRfs.click_on_logout()




@given(u'I can see Group Member contacts on as Activ user')
def step_impl(context):
	raise NotImplementedError(u'STEP: Given I can see Group Member contacts on as Activ user')


@then(u'I verify the contact details for any Member')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I verify the contact details for the Member')