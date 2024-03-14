from baseObjects.baseMethods import BaseMethods
from android_locators import Availability_Locators
from appium import webdriver
from builtins import *
import time


class Availability(BaseMethods):
	def __init__(self, driver: webdriver.Remote):
		self.driver = driver

	def click_on_availability_navigation(self):
		self.perform_action_on_element(locator=Availability_Locators.Bottomnav_availability_tab, action="click")

	def validate_title_on_avalabilitytab(self, department):
		departments = ["All Groups", "Foundational Platforms"]
		if department == "All Groups":
			Title = self.get_element(locator=Availability_Locators.Title_on_availability_tab).text
			print("Title on the Scrren:" + Title)
			print("Title Expected:" + departments[0])
			assert Title == departments[0]

		elif department == "Foundational Platforms":
			Title = self.get_element(locator=Availability_Locators.Title_on_availability_tab).text
			print(Title)
			print(departments[1])
			assert Title == departments[1]

	def click_on_groups_icon(self):
		self.perform_action_on_element(locator=Availability_Locators.Group_selection_icon, action='click')

	def view_my_groups(self):
		# Selecting from the top corner:

		self.is_element_visible(Availability_Locators.Select_all_groups)
		self.is_element_visible(Availability_Locators.Select_foundational_platforms)
		self.is_element_visible(Availability_Locators.Select_people_and_business)
		self.is_element_visible(Availability_Locators.Select_people_and_culture)
		self.is_element_visible(Availability_Locators.Select_policy_unit)
		self.is_element_visible(Availability_Locators.Select_all_groups)
	def select_my_group(self, department):
		Groups = ["All Groups", "Foundational Platforms"]
		print("Selecting My Group: Foundational Platforms from the list")
		self.perform_action_on_element(locator=Availability_Locators.Select_foundational_platforms, action='click')
		if department == "Foundation Platforms":
			Title = self.get_element(locator=Availability_Locators.Title_on_availability_tab).text
			print("Title on the Scrren:" + Title)
			print("Title Expected:" + Groups[1])
			assert Groups[1] == Title


	def select_availability_day_status_from_SET(self):

		print("Selecting Availability from Top Nav Bar: SET | DAY, STATUS")
		self.perform_action_on_element(locator=Availability_Locators.SET_from_top_nav, action='click')
		self.perform_action_on_element(locator=Availability_Locators.SET_day_select, action='click')
		print("Setting the Status to Available")
		self.perform_action_on_element(locator=Availability_Locators.SET_status_available, action='click')

	def select_availability_time_from_SET(self):

		# time_from = self.get_element(locator=Availability_Locators.SET_clock_bar_from).text
		#         # time_to = self.get_element(locator=Availability_Locators.SET_clock_bar_to).text
		#         #
		#         # print("Setting the Start time")

		print("Setting the Start and End Time")
		# Check if the clock bar displays "9:00"
		while "0900" not in self.get_element(locator=Availability_Locators.SET_clock_bar_from).text:
			# Find and click the "+" button element
			plus_button = self.get_element(locator=Availability_Locators.SET_time_plus_button)
			plus_button.click()

			# Wait for a short period to allow the clock bar to update
			time.sleep(1)

		# END TIME SELECTION : 9:00 PM
		print("Setting the End time")
		while "2100" not in self.get_element(locator=Availability_Locators.SET_clock_bar_to).text:
			# Find and click the "-" button element
			Minus_button = self.get_element(locator=Availability_Locators.SET_time_minus_button)
			Minus_button.click()

			# Wait for a short period to allow the clock bar to update
			time.sleep(1)

	def save_availability_from_SET(self):
		print("Saving the availability for, Top Nav Bar: SET")
		self.perform_action_on_element(locator=Availability_Locators.Save_availability, action='click')

		print("Waiting for prompt: Availability Saved")
		self.driver.implicitly_wait(12)

	def select_availability_from_WEEKLY(self):
		print("Moving into Top Nav Bar: WEEKLY")
		self.perform_action_on_element(locator=Availability_Locators.WEEKLY_from_top_nav, action='click')
