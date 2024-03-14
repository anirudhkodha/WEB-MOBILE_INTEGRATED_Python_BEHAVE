import logging
import random
import re
import string
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

RunTimeValue = ""


class NoSuchActionExist(Exception):
	pass


class AllItemsLoaded(Exception):
	print("All page items loaded")


class BaseMethodsWeb:
	def __init__(context, driver: webdriver):
		context.Browserdriver= driver

	def attach_driver(context, driver: webdriver):
		context.Browserdriver = driver

	def detach_driver(context, driver: webdriver):
		context.driver = None

	def _execute_with_wait(context, condition):
		return WebDriverWait(context.Browserdriver,40).until(condition)

	def _execute_with_long_wait(context, condition):
		return WebDriverWait(context.Browserdriver,45).until(condition)

	def wait_for_element(context, locator):
		context._execute_with_wait(ec.presence_of_element_located((locator.l_type, locator.selector)))

	def long_wait_for_element(context, locator):
		context._execute_with_long_wait(ec.presence_of_element_located((locator.l_type, locator.selector)))

	def count_all_elements(context, locator):
		return len(context.Browserdriver.find_elements(locator.l_type, locator.selector))

	def get_all_elements(context, locator):
		return context.Browserdriver.find_elements(locator.l_type, locator.selector)

	def get_elements_inside(context, parent_locator, children_locator):
		return context.Browserdriver.find_element(parent_locator.l_type, parent_locator.selector).find_elements(
			children_locator.l_type, children_locator.selector)

	def get_elements_inside_element(context, parent_element, children_locator):
		return parent_element.find_elements(children_locator.l_type, children_locator.selector)

	def get_element_inside_element(context, parent_element, children_locator):
		return parent_element.find_element(children_locator.l_type, children_locator.selector)

	def element_exists(context, locator):
		try:
			context._execute_with_wait(ec.presence_of_element_located((locator.l_type, locator.selector)))
			return True
		except TimeoutException:
			return False

	def is_element_visible(context, locator):
		try:
			time.sleep(5)
			context._execute_with_wait(ec.visibility_of_element_located((locator.l_type, locator.selector)))
			return True
		except TimeoutException:
			return False

	def get_element(context, locator, text=""):
		if "ObjectToken" in locator.selector:
			locator.selector = locator.selector.replace("ObjectToken", RunTimeValue)
		isExist = context.element_exists(locator)
		if not isExist:
			raise NoSuchElementException("Could not find ->" + locator.selector)
		return context.Browserdriver.find_element(locator.l_type, locator.selector)

	def get_window_size(context):
		return context.Browserdriver.get_window_size()
	#
	# # def swipe(context, start_x, start_y, end_x, end_y, duration=600):
	# # 	action = TouchAction(context.Browserdriver)
	# # 	# It is compulsory to add duration here, otherwise it will not display in the avd emulator
	# # 	action.press(x=start_x, y=start_y).wait(duration).move_to(x=end_x, y=end_y).release()
	# # 	action.perform()
	#
	# # def scroll(context, direction="Down", distance=0.8):
	# # 	window_size = context.get_window_size()
	# # 	midpoint_x = window_size['width'] * 0.5
	# # 	midpoint_y = window_size['height'] * 0.5
	# # 	top = midpoint_y - window_size['height'] * distance * 0.5
	# # 	bottom = midpoint_y + window_size['height'] * distance * 0.5
	# # 	left = midpoint_x - window_size['width'] * distance * 0.5
	# # 	right = midpoint_x + window_size['width'] * distance * 0.5
	# # 	if direction == "Up":
	# # 		context.swipe(midpoint_x, top, midpoint_x, bottom)
	# # 	elif direction == "Down":
	# # 		context.swipe(midpoint_x, bottom, midpoint_x, top)
	# # 	elif direction == "Left":
	# # 		context.swipe(left, midpoint_y, right, midpoint_y)
	# # 	elif direction == "Right":
	# # 		context.swipe(right, midpoint_y, left, midpoint_y)
	#
	# def tap_in_element(context, element):
	# 	rect = element.rect
	# 	midpoint_x = rect['x'] + rect['width'] * 0.5
	# 	midpoint_y = rect['y'] + rect['height'] * 0.5
	# 	context.Browserdriver.execute_script('mobile:tap', {'x': midpoint_x, 'y': midpoint_y, 'element': element})
	#
	# # def scroll_in_element(context, element, direction="Right", distance=0.8):
	# # 	rect = element.rect
	# # 	midpoint_x = rect['x'] + rect['width'] * 0.5
	# # 	midpoint_y = rect['y'] + rect['height'] * 0.5
	# # 	top = midpoint_y - rect['height'] * distance * 0.5
	# # 	bottom = midpoint_y + rect['height'] * distance * 0.5
	# # 	left = midpoint_x - rect['width'] * distance * 0.5
	# # 	right = midpoint_x + rect['width'] * distance * 0.5
	# # 	if direction == "Up":
	# # 		context.swipe(midpoint_x, top, midpoint_x, bottom)
	# # 	elif direction == "Down":
	# # 		context.swipe(midpoint_x, bottom, midpoint_x, top)
	# # 	elif direction == "Left":
	# # 		context.swipe(left, midpoint_y, right, midpoint_y)
	# # 	elif direction == "Right":
	# # 		context.swipe(right, midpoint_y, left, midpoint_y)
	#
	# def scroll_ios(context):
	# 	context.Browserdriver.execute_script('mobile: scroll', {'direction': 'down'})
	#
	# def scroll_to_element_ios(context, predicate):
	# 	context.Browserdriver.execute_script('mobile: scroll', {'direction': 'down', 'predicateString': predicate})

	def get_element_text(context, locator):
		if "ObjectToken" in locator.selector:
			locator.selector = locator.selector.replace("ObjectToken", RunTimeValue)
		if not context.element_exists(locator):
			raise NoSuchElementException("Could not find {locator.selector}")

		context.Browserdriver.find_element(locator.l_type, locator.selector).text

	def get_dynamic_text_from_element(context, locator, text):
		global RunTimeValue
		RunTimeValue = text
		dynamic_text = context.get_element(locator, text).text
		locator.selector = re.sub(r"'[A-Z _/a-z]+'", "'ObjectToken'", locator.selector)
		return dynamic_text

	def wait_for_page_load(context):
		page_state = context.Browserdriver.execute_script('return document.readyState;')
		if page_state == 'complete':
			return WebDriverWait(context.Browserdriver,40)


	def enter_text_in_dynamic_field(context, locator, text_to_locate_element, text_to_enter):
		global RunTimeValue
		RunTimeValue = text_to_locate_element
		context.get_element(locator).send_keys(text_to_enter)
		# locator.selector = locator.get_original_selector()

	def multi_select_for_dynamic_element(context, main_element, option_to_select):
		ActionChains(context.Browserdriver).move_to_element(context.Browserdriver.find_element_by_xpath(
			"//div[text()='" + main_element + "']/following-siblisng::div//li//span[contains(text(),'" +
			option_to_select + "')]")).click().perform()
	#
	# def move_slide_bar(context, element, distance):
	# 	rect = element.rect
	# 	start_x = rect['x']
	# 	end_y = rect['width']
	# 	position = rect['y']
	# 	action = TouchAction(context.Browserdriver)
	# 	action.press(x=start_x, y=position).wait(600).move_to(x=end_y * distance, y=position).release()
	#
	def perform_action_on_element(context, locator, action: str, text="", text_to_enter=""):
		try:
			global RunTimeValue
			flag = False
			RunTimeValue = text
			action = action.lower()
			if "ObjectToken" in locator.selector:
				flag = True
			if action == "click":
				context.get_element(locator).click()
			elif action == "dblclick":
				context.get_element(locator).click()
				time.sleep(1)
				context.get_element(locator).click()
			elif action == "get_text":
				value = context.get_element_text(locator)
				# locator.selector = locator.get_original_selector()
				return value
			elif action == "execute_script_click":
				context.Browserdriver.execute_script("arguments[0].click();", context.get_element(locator))
			elif action == "type":
				context.get_element(locator).send_keys(text)
			elif action == "type_with_generic_locator":
				context.get_element(locator).send_keys(text_to_enter)
			elif action == "clear":
				context.get_element(locator).clear()
			elif action == "ctra_delete":
				ActionChains(context.Browserdriver).key_down(Keys.CONTROL).send_keys('a').perform()
				ActionChains(context.Browserdriver).send_keys(Keys.DELETE).perform()
			elif action == "clickwithactionclass":
				ActionChains(context.Browserdriver).move_to_element(context.get_element(locator)).click().perform()
			# elif action == "long-press":
			# #     ActionChains(context.Browserdriver).longPress(context.get_element(locator)).release().perform()
			# elif action == "scroll":
			# 	context.Browserdriver.execute_script("arguments[0].scrollIntoView(true)", context.get_element(locator))
			# elif action == "scroll_into_middle":
			# 	view_port_height = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
			# 	element_top = "var elementTop = arguments[0].getBoundingClientRect().top;"
			# 	js_function = "window.scrollBy(0, elementTop-(viewPortHeight/2));"
			# 	scroll_into_middle = view_port_height + element_top + js_function
			# 	context.Browserdriver.execute_script(scroll_into_middle, context.get_element(locator))
			elif "switch_tab" == action:
				ActionChains(context.Browserdriver).key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(
					Keys.CONTROL).perform()
			elif action == "press_enter":
				ActionChains(context.Browserdriver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
			elif action == "press_end":
				ActionChains(context.Browserdriver).key_down(Keys.END).key_up(Keys.END).perform()
			elif action == "present":
				try:
					assert context.get_element(locator).is_displayed()
				except:
					print(text + " -> Element is not displayed on the page")
					assert False, text + " Element is not displayed on the page"
			elif action == "not_present":
				if context.count_all_elements(locator) == 0:
					assert True, "User does not have access to current action. PASSED"
				else:
					assert False, text + " Element is displayed on the page which is invalid in this case. FAILED"
			elif action == "not_display":
				if "ObjectToken" in locator.selector:
					locator.selector = locator.selector.replace("ObjectToken", RunTimeValue)
				number_of_elements = context.Browserdriver.find_elements_by_xpath(locator.selector)
				if len(number_of_elements):
					assert False, "Element is displayed on the page. FAILED"
				else:
					assert True, "Element is not displayed on the page. PASSED"
			else:
				raise NoSuchActionExist(action)
			# if flag:
			#     locator.selector = locator.get_original_selector()
		except:
			# locator.selector = locator.get_original_selector()
			logging.info(action + " on " + str(locator.selector) + " is not working")
			assert False, action + " on " + str(locator.selector) + " is failing"

	def get_random_string(context, length):
		letters = string.ascii_lowercase
		return ''.join(random.choice(letters) for i in range(length))

	def success_print(context, message):
		print(message)
		return True

	def assert_equal(context, actual, expected, error_message=None, success_message=None):
		error_message = "Assertion Failed : Actual value : " + str(actual) + " , Expected Value : " + str(
			expected) + ", Error Message : " + str(error_message)
		success_message = "Assertion Passed : Actual value : " + str(actual) + " , Expected Value : " + str(
			expected) + ", Success Message : " + str(success_message)
		assert actual == expected and context.success_print(success_message), error_message

	def assert_not_equal(context, actual, expected, error_message=None, success_message=None):
		error_message = "Assertion Failed : Actual value : " + str(actual) + " , Expected Value : " + str(
			expected) + ", Error Message : " + str(error_message)
		success_message = "Assertion Passed : Actual value : " + str(actual) + " , Expected Value : " + str(
			expected) + ", Success Message : " + str(success_message)
		assert actual != expected and context.success_print(success_message), error_message
	#
	# def app_active(context):
	#
	# 	context.Browserdriver.activate_app('')
