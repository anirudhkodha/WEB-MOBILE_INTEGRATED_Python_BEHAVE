import time
from behave import *
from pages.android.Member_Login_Navigation_page import Login_feature


@given('I login to rfs activ with "{username}" and "{password}"')
def login_to_activ(context, username, password):
    # time.sleep(2)
    # retry_num = 0
    context.loginPageRfs = Login_feature(context.driver)
    context.loginPageRfs.click_login()
    print(context.driver.current_context)
    context.loginPageRfs.login(username, password)


@given('I can see Group Member contacts on as Activ user')
def activ_page_details(context):
    context.loginPageRfs = Login_feature(context.driver)
    context.loginPageRfs.click_on_menu_icon()
    context.loginPageRfs.click_on_menu_icon()
    context.loginPageRfs.click_on_menu_contacts()
    context.loginPageRfs.search_contact()


@then('I verify the contact details for the Member')
def verify_contact_details(context):
    context.loginPageRfs = Login_feature(context.driver)
    context.loginPageRfs.click_on_contact()

    context.loginPageRfs = Login_feature(context.driver)
    # loginPageRfs.verify_contact_details()
    context.driver.back()


@given('I click on QuickView')
def inside_quickview(context):
    time.sleep(5)
    context.loginPageRfs = Login_feature(context.driver)
    context.loginPageRfs.click_on_quickview()


@given('I click on ListView')
def inside_listview(context):
    context.loginPageRfs = Login_feature(context.driver)
    context.loginPageRfs.click_on_listview()


@then('I logout as a member')
def logout(context):
    # click on MenuIcon
    context.loginPageRfs = Login_feature(context.driver)
    context.loginPageRfs.click_on_menu_icon()
    # click on settings
    context.loginPageRfs = Login_feature(context.driver)
    context.loginPageRfs.click_on_settings()
    # logout
    context.loginPageRfs = Login_feature(context.driver)
    time.sleep(4)
    context.loginPageRfs.click_on_logout()
