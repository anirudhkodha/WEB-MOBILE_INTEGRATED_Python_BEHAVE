import time
from baseObjects.baseMethods import BaseMethods
from android_locators import Login_Activ, Menu_Navigations
from appium import webdriver
from builtins import *
from settings.config import script_settings


class Login_feature(BaseMethods):

	def __init__(self, driver: webdriver.Remote):
		self.driver = driver

	def click_login(self):
		print("Clicking on First login button")


		self.wait_for_element(locator=Login_Activ.Login_Button_First_Screen)
		self.perform_action_on_element(locator=Login_Activ.Login_Button_First_Screen, action="click")
		print("Login button clicked to go for the Credenntials Check")

	def login(self, username, password):
		print("Checking if Oauth Screen appears")

		time.sleep(5)
		print("Current View:" + self.driver.current_context)

		print('Entering the Credentials')
		# Member ID input field #
		self.is_element_visible(locator=Login_Activ.MemberIdInput)
		if username == 'username':
			username = script_settings['standard_member']['username_01']
		member_id_field = self.get_element(locator=Login_Activ.MemberIdInput)
		member_id_field.clear().send_keys(username)

		# Member password input field #
		self.is_element_visible(locator=Login_Activ.PasswordInput)
		if password == 'password':
			password = script_settings['standard_member']['password_01']
		password_field = self.get_element(locator=Login_Activ.PasswordInput)
		password_field.clear().send_keys(password)
		print("Credentials Entered and Clicking on Login Button")
		self.perform_action_on_element(locator=Login_Activ.Login_Button_Second_Screen, action="click")

	def click_on_quickview(self):
		# QUICK VIEW
		print("Checking if QuickView Layout is visible")
		self.is_element_visible(locator=Menu_Navigations.Quick_view_image)
		# QuickViewText = self.get_element(locator=Menu_Navigations.Quick_view_Text).text
		# assert QuickViewText == "Quick View"
		self.perform_action_on_element(locator=Menu_Navigations.Quick_view_image, action='click')
		print("Clicking on QuickView Layout")


	def click_on_listview(self):
		# LIST VIEW
		# ListViewText = self.get_element(locator=Menu_Navigations.List_view).text
		# assert ListViewText == "List View"
		print("Checking if ListView Layout is visible")
		self.is_element_visible(locator=Menu_Navigations.List_view_image)
		print("Clicking on ListView Layout")
		self.perform_action_on_element(locator=Menu_Navigations.List_view_image, action='click')

	def click_on_menu_icon(self):
		self.perform_action_on_element(locator=Menu_Navigations.Menu_icon, action='click')

	def click_on_menu_contacts(self):
		self.perform_action_on_element(locator=Menu_Navigations.Menu_contacts, action='click')

	def search_contact(self):
		ContactSearch = self.get_element(locator=Menu_Navigations.Search_contacts_field)
		ContactSearch.send_keys('War')

	def click_on_contact(self):
		self.perform_action_on_element(locator=Menu_Navigations.Contact_name, action='click')

	def verify_contact_details(self):
		Conntact_info = ["Warid", "Islam", "warid.islam@rfs.nsw.gov.au", "0405019666"]

		FN = self.get_element(locator=Menu_Navigations.Contact_info_FN).text
		print(FN)
		assert FN == Conntact_info[0]

	def click_on_settings(self):
		self.perform_action_on_element(locator=Menu_Navigations.Sidebar_settings, action='click')

	def click_on_logout(self):
		self.perform_action_on_element(locator=Menu_Navigations.Scrollto_logout_button, action='click')
		self.perform_action_on_element(locator=Menu_Navigations.Confirm_logout, action='click')

		#
		# def scroll_to_logout(self):
		#
		#     actions = TouchAction(self.driver)
		#     for X in range(1):
		#         actions.press(x=542, y=1705).move_to(x=542, y=797).release().perform()

		# visibility = False
		# i = 0

		# while not visibility or i < 100:
		#     i += 1
		#     try:
		#         TouchAction(self.driver).press(x=548, y=490).move_to(x=514, y=1550).release().perform()

		#     except:
		#         visibility = self().is_element_visible(locator=Menu_Navigations.Logout_button)

		# if not visibility:
		#     print("not found")
		# el1 = self().get_element(locator=Menu_Navigations.Settings_name)
		# el2 = self().get_element(locator=Menu_Navigations.Settings_discussion)
		# action = TouchAction(self.driver)
		# action.press(el2).move_to(el1).release().perform()
		# self.driver.execute_script('mobile: scrollTo', el2.id)
		# landing back on login page
		# return self().is_element_visible(locator=Login_Logout_Activ.Login_Button_Second_Screen) is True
