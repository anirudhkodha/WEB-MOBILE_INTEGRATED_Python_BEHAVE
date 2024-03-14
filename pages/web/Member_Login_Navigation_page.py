from selenium import webdriver
from selenium.webdriver import Keys

from baseObjects.baseMethods_web import BaseMethodsWeb
from settings.config import script_settings
from  web_locators import Login_logout_Web


class Login_feature(BaseMethodsWeb):

	def click_login(context):
		context.wait_for_page_load()
		context.wait_for_element(locator=Login_logout_Web.Login_Button)
		print("Cliicking on login button")
		context.perform_action_on_element(locator=Login_logout_Web.Login_Button, action="click")
		print("Login button clicked to go for the Credenntials Check")
#
# 	def click_on_quickview(context):
# 		# QUICK VIEW
# 		print("Checking if QuickView Layout is visible")
# 		context.is_element_visible(locator=Menu_Navigations.Quick_view_layout)
# 		print("Clicking on QuickView Layout")
# 		context.perform_action_on_element(locator=Menu_Navigations.Quick_view_layout, action='click')
#
#
# #**************************************************************************************************************************************
# # def Auth0_login(context):
# # 	auth0 = ('YOUR_AUTH0_DOMAIN', 'YOUR_AUTH0_CLIENT_ID')
# #
# # 	# Obtain the login credentials (email and password) from your test data or configuration
# # 	email = 'your_email@example.com'
# # 	password = 'your_password'
# #
# # 	# Perform the Auth0 login
# # 	auth0.login(email=email, password=password)
# #
# # 	# Wait for the login to complete (e.g., wait for the dashboard screen to appear)
# # 	dashboard_screen = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'your_dashboard_screen_id')))
# #**************************************************************************************************************************************
#
#
	def login(context, username, password):
		context.attach_driver(context.Browserdriver)

		print("Checking if Oauth Screen appears")

		if context.is_element_visible(locator=Login_logout_Web.MemberIdInput) == True:
			print('USERNAME AND PASSWORD fields available to Enter the Credentials')
			# Member ID input field #
		if username == 'username':
			username = script_settings['standard_member']['username_01']
		member_id_field = context.get_element(locator=Login_logout_Web.MemberIdInput)
		member_id_field.send_keys(username)

		# Member password input field #
		if password == 'password':
			password = script_settings['standard_member']['password_01']
		password_field = context.get_element(locator=Login_logout_Web.PasswordInput)
		password_field.send_keys(password)
		password_field.send_keys(Keys.RETURN)


			# context.perform_action_on_element(locator=Login_Logout_Activ.Login_Button_Second_Screen, action="click")
		# else:
		# 	context.perform_action_on_element(locator=Login_logout_Web.Oauth_Not_Your_Account, action='click')
# 	def click_on_listview(context):
# 		context.perform_action_on_element(locator=Menu_Navigations.List_view_layout, action='click')
#
#
# 	def click_on_menu_icon(context):
#
# 		context.perform_action_on_element(locator=Menu_Navigations.Menu_icon, action="click")
#
# 	def click_on_settings(context):
# 		context.perform_action_on_element(locator=Menu_Navigations.Menu_settings_button, action='click')
#
#
# 	def click_on_logout(context):
# 		# context.driver.execute_script("arguments[0].scrollIntoView(true)", context.get_element(Menu_Navigations.Logout_button))
# 		# context.scroll(direction= 'down', duration= 0.8)
# 		context.scroll_to_element_ios(predicate= 'label == "Log Off " AND name == "btn_setting_"')
#
# 		context.wait_for_element(locator=Menu_Navigations.Logout_button)
# 		context.perform_action_on_element(locator=Menu_Navigations.Logout_button, action='click')
# 		# context.wait_for_element(locator=Menu_Navigations.Confirm_Logout_button)
# 		# context.perform_action_on_element(locator=Menu_Navigations.Confirm_Logout_button, action='click')

