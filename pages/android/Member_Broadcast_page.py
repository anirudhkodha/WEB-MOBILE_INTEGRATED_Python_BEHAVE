import time
from baseObjects.baseMethods import BaseMethods
from appium import webdriver
from android_locators import *
from builtins import *
from mapbox import Directions
from selenium.webdriver import *



class Broadcast(BaseMethods):
	def __init__(self, driver: webdriver.Remote):
		self.driver = driver

	def click_on_broadcast_navigation(self):
		self.perform_action_on_element(locator=Menu_Navigations.Bottomnav_broadcast_tab, action="click")
	def plus_button_broadCast(self):
		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Listview_plus_button, action='click')
		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Listview_plus_button_broadcast, action='click')

	def broadcast_alert(self, ):

		#[[[[[[[ To_Elements = self.driver.find_elements(ListView_PlusButton_Broadcast_Locators.Listview_plus_button_broadcast_to_Select)
		# check_symbol = None
		# for element in To_Elements:
		# 	Text = element.get_attribute("text")
		# 	if "" in Text:
		# 		check_symbol = Text
		# 		break
		# 	print(check_symbol)]]]]]


		BRG:list =self.get_all_elements(locator=ListView_PlusButton_Broadcast_Locators.Listview_plus_button_broadcast_to)
		for i in range(len(BRG)):
			BRG_name_inside = BRG[i].get_attribute("text")

		if "ACTIV BRG Foundational Platforms" in BRG_name_inside:
			print('Found the BRG')

		# assert BRG[1] == "ACTIV BRG Foundational Platforms"
		# else:
		# 	self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Listview_plus_button_broadcast_to , action='click')q
		# 	self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Listview_plus_button_broadcast_to_Select, action='click')
		# 	self.driver.back()

		# BRG = self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Listview_plus_button_broadcast_to_seleected, action='get_text')
		# assert BRG == "ACTIV BRG Foundational Platforms"

		# LOCATIONS
		time.sleep(5)
		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.ListView_plus_button_broadcast_Location, action='click')
		search_field = self.get_element(locator=ListView_PlusButton_Broadcast_Locators.ListView_plus_button_broadcast_Location_search)
		search_field.send_keys("PENRITH")

		if self.get_element(locator=ListView_PlusButton_Broadcast_Locators.Location_popup_allow).is_displayed():
			self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Location_popup_allow, action="click")

		# search_penrith = self.get_element(locator=ListView_PlusButton_Broadcast_Locators.Location_search)
		# search_penrith.send_keys(Keys.ENTER)
		# locationprompt = self.get_element(locator=Maps.Map_prompts_allow).is_displayed()
		# if locationprompt == True:
		# 	self.perform_action_on_element(locator=Maps.Map_prompts_allow, action='click')
		time.sleep(15)
		# Penrith_to_select
		self.wait_for_element(locator=ListView_PlusButton_Broadcast_Locators.ListView_plus_button_broadcast_Location_Select)
		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.ListView_plus_button_broadcast_Location_Select, action='click')
		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.ListView_plus_button_broadcast_Location_Select, action='click')
		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Add, action='click')

		# Coords value check
		# Coords_destination = self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Coord_bradcast, action='get_text')
		# Then AdD Location
 		# self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Add, action='click')

		# Location = self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Location_confirm, action='get_text')
		# if 'Penrith' in Location:
		# 	print("Location is selected as Penrith")
		# else:
		# 	print("Location is not selected as Penrith")

		# IGNORE for demo

		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Alert, action='click')
		time.sleep(5)
		Toogle_on = self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Alert, action='get_text')
		print(Toogle_on)


		print('start to uplaod image')

		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Attachment, action='click')
		# File uplopading
		# dest_path = '/sdcard/Pictures/Android_O.png'
		# self.driver.push_file(dest_path, '')
		file_upload_element = self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.upload_image, action='click' )
		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.upload_image_folders, action='click')
		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.image_select,action='click')
		time.sleep(5)
		print('image uploaded')
		# Trigger the file selection dialog
		# file_upload_element.click()
		# Handle the file selection dialog
		# file_selection_dialog = self.driver.switch_to.alert
		# Set the file path for upload
		# file_path = '/sdcard/Pictures/Android_O.png'  # Specify the file path of the file you want to upload
		# file_selection_dialog.send_keys(file_path)
		# # Initiate the upload
		# file_selection_dialog.accept()

		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Broadcast_Message, action='type_text', text=ListView_PlusButton_Broadcast_Locators.Broadcast_name)
		time.sleep(2)
		Alert_Message = self.get_element(locator=ListView_PlusButton_Broadcast_Locators.Broadcast_Message).text
		self.perform_action_on_element(locator=ListView_PlusButton_Broadcast_Locators.Broadcast_Send, action='click')
		# Broadcast_new_ = self.driver.find_elements(locator=Broadcast_Group_Listview.Recent_Broadcast_Tile)
		# if Alert_Message in Broadcast_new_:
		# 	print("Broadcast is sent successfully")

	def broadcast_alert_component(self):
		Recet_broadcast = self.is_element_visible(locator=Broadcast_Group_Listview.Recent_Broadcast_Tile)
		Accept_button = self.is_element_visible(locator=Broadcast_Group_Listview.Accept_button)
		Decline_button = self.is_element_visible(locator=Broadcast_Group_Listview.Decline_button)
		Other_button = self.is_element_visible(locator=Broadcast_Group_Listview.Other_button)
		Options_button = self.is_element_visible(locator=Broadcast_Group_Listview.Options_button)
		Map_button = self.is_element_visible(locator=Broadcast_Group_Listview.Map_button)

		Broadcast_Components = [Recet_broadcast, Accept_button, Decline_button, Other_button, Options_button, Map_button]

		if all(Broadcast_Components):
			print("All the components are present in the broadcast alert")

		else:
			print("All the components are not present in the broadcast alert")

	def broadcast_alert_accept(self):
		self.perform_action_on_element(locator=Broadcast_Group_Listview.Accept_button, action='click')
		self.wait_for_element(locator=Broadcast_Group_Listview.Attendance_Logged)
		Attendance_Logged = self.is_element_visible(locator=Broadcast_Group_Listview.Attendance_Logged)
		if Attendance_Logged == True:
			print("Attendance is logged")
	def broadcast_alert_map(self):
		self.perform_action_on_element(locator=Broadcast_Group_Listview.Map_button, action='click')
		Map_permission = self.is_element_visible(locator=Maps.Map_prompts_allow)
		if Map_permission == True:
			self.perform_action_on_element(locator=Maps.Map_prompts_allow, action='click')
			self.driver.back()
			self.perform_action_on_element(locator=Broadcast_Group_Listview.Map_button, action='click')

		print("Checking Map Elements")
		for locator in Maps.Map_elements_all:
			Map_elements_on_screen = self.driver.find_element(*locator)

			if Map_elements_on_screen.is_displayed():
				print("Map Componetnts is displayed")
			else:
				print("Map Componetnts is not displayed")


		print("Checking Map Distances")

		mapbox_access_token = 'sk.eyJ1Ijoid2FyaWRpc2xhbSIsImEiOiJjbGptcHVvNnUxMHd6M2ZsNTExdHhhM2FiIn0.lRUNgWlQJXPGpxC9chfF4A'
		self.perform_action_on_element(locator=Maps.My_Loc_icon, action='dblclick')
		Distance_value = self.is_element_visible(locator=Maps.Distance).text
		ETA_value = self.is_element_visible(locator=Maps.ETA).text

		# desired Destination location for direction
		origin = [-33.8679, 151.2069]
		destination = [-33.75374,150.69821]

		# Initialize the Mapbox Directions client
		directions = Directions(access_token=mapbox_access_token)

		# Request the route between the origin and destination
		response = directions.directions(
			coordinates=[origin, destination],
			profile='mapbox/driving-traffic',
		)
		# Retrieve the direction line information from the response


		geojson_response = response.json()
		print(geojson_response)

		self.driver.back()

	# Perform assertions on the direction line
	# ... (Implement your assertions here)

	def broadcast_attendance_details(self):
		self.perform_action_on_element(locator=Broadcast_Group_Listview.Recent_Broadcast_Tile, action='click')
		self.wait_for_element(locator=Broadcast_Group_Listview.Attendance_Logged)

		Attending_rows = self.get_element(locator=Broadcast_Group_Listview.Attending)
		Attending_rows_count = len(Attending_rows)
		Warid_Attending_row= None

		for row in Attending_rows:
			text = row.get_attribute('text')
			if 'Warid Islam' in text:
				Warid_Attending_row = row
				break

			if Warid_Attending_row is not None:
				# Warid Islam element found
				# Perform desired actions
				print("Warid Islam is present in the label of an element with name starting with 'row_attend_'")
			else:
				# Warid Islam element not found
				print("No element with name starting with 'row_attend' has label containing 'Warid Islam'")

			Warid_Attending_row.click()

		print("Checking the elements INSIDE e attendance member details screen")

		for locator in Broadcast_Group_Listview.Attendance_details:
			Attendance_Member_details_on_screen = self.get_all_elements(locator=locator)

			if Attendance_Member_details_on_screen.is_displayed():
				print("Attendance Member details is displayed")
			else:
				print("Attendance Member details is not displayed")

		for i in range(2):
			self.driver.back(i)