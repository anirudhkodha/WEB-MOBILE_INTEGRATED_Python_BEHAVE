from builtins import *
from appium import webdriver
from selenium.webdriver import Keys
from baseObjects.baseMethods import BaseMethods
from ios_locators import Menu_Navigations
from ios_locators import Login_Logout_Activ
from settings.config import script_settings


class Login_feature(BaseMethods):
	def __init__(self, driver: webdriver.Remote):
		self.driver = driver


	def click_login(self):
		print("Clcficking on First login button")
		self.perform_action_on_element(locator=Login_Logout_Activ.Login_Button_First_Screen, action="click")
		print("Login button clicked to go for the Credenntials Check")


	def login(self, username, password):
		print("Checking if Oauth Screen appears")
		if self.is_element_visible(locator=Login_Logout_Activ.MemberIdInput) == True:

			print("Current View:" + self.driver.current_context)

			print('Entering the Credentials')
			# Member ID input field #
			self.is_element_visible(locator=Login_Logout_Activ.MemberIdInput)
			if username == 'username':
				username = script_settings['standard_member']['username_01']
			member_id_field = self.get_element(locator=Login_Logout_Activ.MemberIdInput)
			member_id_field.send_keys(username)

		# Member password input field #
			self.is_element_visible(locator=Login_Logout_Activ.PasswordInput)
			if password == 'password':
				password = script_settings['standard_member']['password_01']
			password_field = self.get_element(locator=Login_Logout_Activ.PasswordInput)
			password_field.send_keys(password)
			password_field.send_keys(Keys.RETURN)
			# self.perform_action_on_element(locator=Login_Logout_Activ.Login_Button_Second_Screen, action="click")
		else:
			self.perform_action_on_element(locator=Login_Logout_Activ.Oauth_Not_Your_Account, action='click')


#**************************************************************************************************************************************
# def Auth0_login(self):
# 	auth0 = ('YOUR_AUTH0_DOMAIN', 'YOUR_AUTH0_CLIENT_ID')
#
# 	# Obtain the login credentials (email and password) from your test data or configuration
# 	email = 'your_email@example.com'
# 	password = 'your_password'
#
# 	# Perform the Auth0 login
# 	auth0.login(email=email, password=password)
#
# 	# Wait for the login to complete (e.g., wait for the dashboard screen to appear)
# 	dashboard_screen = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'your_dashboard_screen_id')))
#**************************************************************************************************************************************


	def click_on_quickview(self):
		# QUICK VIEW
		print("Checking if QuickView Layout is visible")
		self.is_element_visible(locator=Menu_Navigations.Quick_view_layout)
		print("Clicking on QuickView Layout")
		self.perform_action_on_element(locator=Menu_Navigations.Quick_view_layout, action='click')
	def click_on_listview(self):
		self.perform_action_on_element(locator=Menu_Navigations.List_view_layout, action='click')


	def click_on_menu_icon(self):

		self.perform_action_on_element(locator=Menu_Navigations.Menu_icon, action="click")

	def click_on_settings(self):
		self.perform_action_on_element(locator=Menu_Navigations.Menu_settings_button, action='click')


	def click_on_logout(self):
		# self.driver.execute_script("arguments[0].scrollIntoView(true)", self.get_element(Menu_Navigations.Logout_button))
		# self.scroll(direction= 'down', duration= 0.8)
		self.scroll_to_element_ios(predicate= 'label == "Log Off " AND name == "btn_setting_"')

		self.wait_for_element(locator=Menu_Navigations.Logout_button)
		self.perform_action_on_element(locator=Menu_Navigations.Logout_button, action='click')
		# self.wait_for_element(locator=Menu_Navigations.Confirm_Logout_button)
		# self.perform_action_on_element(locator=Menu_Navigations.Confirm_Logout_button, action='click')

