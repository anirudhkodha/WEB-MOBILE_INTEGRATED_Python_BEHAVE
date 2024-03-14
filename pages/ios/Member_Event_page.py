from appium import webdriver
from selenium.webdriver import Keys
from baseObjects.baseMethods import BaseMethods
from ios_locators import Broadcast_Tab_QuickView , Broadcast_Tab_Inside_Event_Attendance
from ios_locators import Event_Tab_Locators
import builtins
from datetime import datetime, timedelta
class Event_Details(BaseMethods):
	def __init__(self, driver: webdriver.Remote):
		self.driver = driver

	def tap_on_broadcast_navigation(self, bottom_nav):
		if bottom_nav == "Broadcast":
			self.perform_action_on_element(locator=Broadcast_Tab_QuickView.Bottomnav_broadcast_tab, action="click")

	def tap_on_event_navigation(self, bottom_nav):
		if bottom_nav == "Event":
			self.perform_action_on_element(locator=Event_Tab_Locators.Bottomnav_event_tab, action="click")

	def  check_for_event_component(self):
		print("Checking for Event Component on the Screen")

		Attendance_button = self.is_element_visible(locator= Broadcast_Tab_QuickView.Quickviiew_attendance_button)
		Accept_button = self.is_element_visible(locator=Broadcast_Tab_QuickView.Quickviiew_accept_button)
		Declined_button = self.is_element_visible(locator=Broadcast_Tab_QuickView.Quickviiew_declined_button)
		Options_button = self.is_element_visible(locator=Broadcast_Tab_QuickView.Quickviiew_options_button)
		Eventdetails_button = self.is_element_visible(locator=Broadcast_Tab_QuickView.Quickview_eventdetails_button)
	#***************************************************************************************************************************************
		Event_comonents_on_quickview = [Attendance_button,Accept_button,Declined_button,Options_button,Eventdetails_button]

		if all(Event_comonents_on_quickview):
			builtins.print("Event Component is visible on the Screen")

		else:
			builtins.print(f"Component {Event_comonents_on_quickview.__getitem__()} is not visible on the Screen")
	def accept_event(self):
		self.perform_action_on_element(locator=Broadcast_Tab_QuickView.Quickviiew_accept_button, action="click")

	def check_attendance_details(self):

		builtins.print("Checking for Attendance Details on the Screen - Title")
		self.perform_action_on_element(locator=Broadcast_Tab_QuickView.Quickview_eventdetails_button, action="click")
		Title = self.get_element(locator=Broadcast_Tab_Inside_Event_Attendance.Attendance_Page_title, attribute="name")
		assert Title == "Responses"
		builtins.print("Checking for Attendance Details on the Screen - Attending")

		Attending_rows = self.get_element(locator=Broadcast_Tab_Inside_Event_Attendance.Attending)
		Attending_rows_count = len(Attending_rows)
		Warid_Attending_row= None

		for row in Attending_rows:
			label = row.get_attribute('label')
			if 'Warid Islam' in label:
				Warid_Attending_row = row
				break

		if Warid_Attending_row is not None:
			# Warid Islam element found
			# Perform desired actions
			print("Warid Islam is present in the label of an element with name starting with 'row_attend_'")
			Warid_Attending_row.click()

		else:
			# Warid Islam element not found
			print("No element with name starting with 'row_attend' has label containing 'Warid Islam'")


	def click_add_event(self):
		builtins.print(" TAP ON ADD Event ICON ON TOP RIGHT CORNER")
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_btn_ontop, action="click")
	def create_event_initial_steps(self):
		builtins.print("Filling up the Event Details")
		self.get_element(locator=Event_Tab_Locators.Event_tab_addnew_EvtName).send_keys("Test Automation Event" + Keys.ENTER)
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_grpname, action="click")
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_grpname_select, action="click")
		Selected_GROUP = self.get_element(locator=Event_Tab_Locators.Event_tab_addnew_grpname).text
		print(Selected_GROUP)

		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_to, action="click")
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_to_select, action="click")
		self.wait_for_element(locator=Event_Tab_Locators.Event_tab_addnew_type)
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_type, action="click")
		self.scroll_to_element_ios(predicate='label == "Training" AND name == "row_listpicker_EventTypeId_24"')
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_type_select, action="click")

		EVENT_STATUS = self.get_element(locator=Event_Tab_Locators.Event_tab_addnew_status).text
		print(EVENT_STATUS)
		if "Confirmed" in EVENT_STATUS:
			print("Event Status is Confirmed")

		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_Resources, action="click")
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_Resources_select, action="click")
		self.driver.back()

	def Event_date_time_picker(self):
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_Start, action="click")

		# Get the Event date
		future_date = datetime.today() + timedelta(days=4)
		# Format the date
		formatted_date = future_date.strftime("%d %b")
		# Print the formatted date
		print(formatted_date)


		Values = [] = self.get_all_elements(locator=Event_Tab_Locators.Event_tab_DATE)
		Values.get(0).send_keys(formatted_date + Keys.TAB)

		# # DATE, HOUR AND MINUTES  PICKER WHEEL++++++++
		# self.wait_for_element(locator=Event_Tab_Locators.EVENT_date_parent_element)
		# picker_wheel_date = self.get_element(locator=Event_Tab_Locators.EVENT_date_parent_element).text
		# picker_wheel_date.send_keys(formatted_date)
		# picker_wheel_date.send_keys(Keys.TAB)
		# self.wait_for_element(locator=Event_Tab_Locators.EVENT_hour_element)
		# picker_wheel_hour = self.get_element(locator=Event_Tab_Locators.EVENT_hour_element).text
		# picker_wheel_hour.send_keys("10")
		# picker_wheel_hour.send_keys(Keys.TAB)
		# self.wait_for_element(locator=Event_Tab_Locators.Event_minute_element)
		# picker_wheel_minutes = self.get_element(locator=Event_Tab_Locators.Event_minute_element).text
		# picker_wheel_minutes.send_keys("00")


		# # Select the new date in the picker wheel
		# self.driver.execute_script("mobile: selectPickerWheelValue", {"order": "next", "offset": 0.15, "element": picker_wheel_date.text, "value": formatted_date})
		#
		# self.driver.execute_script("mobile: selectPickerWheelValue", {"order": "next", "offset": 0.15, "element": picker_wheel_hour.text, "value": "10:00 o'clock"})
		#
		# self.driver.execute_script("mobile: selectPickerWheelValue", {"order": "next", "offset": 0.15, "element": picker_wheel_minutes.text, "value": "00 minutes"})

	def create_event_last_steps(self):
		#Location
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_location,action="click")
		self.get_element(locator=Event_Tab_Locators.Event_tab_addnew_location_Search).send_keys("Town Hall NSW" + Keys.ENTER)

		if self.get_element(locator=Event_Tab_Locators.Location_popup_allow).is_displayed():
			self.perform_action_on_element(locator=Event_Tab_Locators.Location_popup_allow, action="click")
		self.wait_for_element(locator=Event_Tab_Locators.Event_tab_addnew_location_select)
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_location_select, action="click")
		# self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_location_select, action="click")
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_location_add, action="click")
		Selected_LOCATION = self.get_element(locator=Event_Tab_Locators.Event_tab_addnew_location).text
		Expected_LOCATION = "Town Hall, Sydney"
		if Expected_LOCATION in Selected_LOCATION:
			print("Location is selected")


		#MIN AND MAX MEMBERS
		# self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_MinMembers, action="click")
		# self.driver.execute_script("mobile: selectPickerWheelValue", {"order": "next", "offset": 0.15, "element": Event_Tab_Locators.Selected_Min_Members , "value": "10"})

		# self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_MaxMembers, action="click")
		# self.driver.execute_script("mobile: selectPickerWheelValue", {"order": "next", "offset": 0.15, "element": Event_Tab_Locators.Selected_Max_Members, "value": "40"})



		# future_date = datetime.today() + timedelta(days=3)
		# # Format the date
		# formatted_date_RSVP = future_date.strftime("%a %d %b")
		# # Print the formatted date
		# print(formatted_date_RSVP)
		# self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_addnew_RSVP, action="click")

		# Select the RSVP date in the picker wheel
		# self.driver.execute_script("mobile: selectPickerWheelValue", {"order": "next", "offset": 0.15, "element": Event_Tab_Locators.RSVP_date_parent_element, "value": formatted_date_RSVP})
		# self.driver.execute_script("mobile: selectPickerWheelValue", {"order": "next", "offset": 0.15, "element": Event_Tab_Locators.RSVP_hour_element, "value": "20:00 o'clock"})
		# self.driver.execute_script("mobile: selectPickerWheelValue", {"order": "next", "offset": 0.15, "element": Event_Tab_Locators.Event_minute_element, "value": "00 minutes"})

		# #Select notes TAB
		self.scroll_to_element_ios(predicate= 'label == "Event Notes..." AND name == "txt_edit_event_Notes"')
		self.get_element(locator=Event_Tab_Locators.Event_tab_addnew_notes).send_keys("Test Automation Event")
		#SAVE EVENT
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_save, action="click")
		# self.perform_action_on_element(locator=Event_Tab_Locators.Event_save, action="click")

		#CHECK IF EVENT IS CREATED
		self.perform_action_on_element(locator=Event_Tab_Locators.Event_tab_listview_btn_ontop, action="click")

	# def close_modal(self, action):
	# 	self.perform_action_on_element(locator=Men, action=action)

