from selenium.webdriver import Keys
from baseObjects.baseMethods_web import BaseMethodsWeb
# from selenium import webdriver
from web_locators import *


class Web_Event(BaseMethodsWeb):

	def check_and_click_on_Feeds(context):
		context.attach_driver(context.Browserdriver)
		context.wait_for_page_load()
		context.wait_for_element(locator=Event_Feeds.Event_List)
		name_of_the_alert = context.get_element(locator=Event_Feeds.NAME_OF_Event).text
		print(name_of_the_alert)
		event_grp = context.get_element(locator=Event_Feeds.GRP_OF_EVENT).text
		print(event_grp)
		context.perform_action_on_element(locator=Event_Feeds.Event_List, action="click")


	def tap_on_generate_report(context):
		context.attach_driver(context.Browserdriver)
		context.wait_for_page_load()
		context.wait_for_element(locator=Event_Feeds.Generate_Report)
		context.perform_action_on_element(locator=Event_Feeds.Generate_Report, action="click")

	def Create_event_tapon(context):
		context.attach_driver(context.Browserdriver)
		context.perform_action_on_element(locator=Event_action.NEW_Button, action="click")
		context.perform_action_on_element(locator=Event_action.NEW_Broadcast, action="click")
		context.wait_for_page_load()

	def Enter_event_details(context):
		context.attach_driver(context.Browserdriver)
		Assinged_BRG = context.get_element(locator=Event_action._Grp_To)
		# context.Browserdriver.execute_script("return arguments[0].shadowRoot;", Assinged_BRG)
		if Assinged_BRG.is_displayed():
			print("Element is visible")
		Assinged_BRG.select_by_visible_text('ACTIV BRG Foundational Platform')
		# Assinged_BRG.send_keys('ACTIV BRG'+Keys.ENTER).implicitly_wait(30)
		# Assinged_BRG.click()
		# Assigned_BRG = context.Browserdriver.execute_script("return document.querySelector(\"span[class='select2 select2-container select2-container--bootstrap select2-container--below select2-container--focus'] ul[class='select2-selection__rendered']\")")
		# Assigned_BRG.click()
		# context.get_element(locator=Event_action.Message_box).send_keys("This is AUTOMATION Test message")