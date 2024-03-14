import logging
import random
import re
import string
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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


class BaseMethods:
	def __init__(self, driver: webdriver):
		self.driver = None  # type: webdriver

	def attach_driver(self, driver: webdriver):
		self.driver = driver

	def detach_driver(self, driver: webdriver):
		self.driver = None

	def _execute_with_wait(self, condition):
		return WebDriverWait(self.driver,40).until(condition)

	def _execute_with_long_wait(self, condition):
		return WebDriverWait(self.driver,45).until(condition)

	def wait_for_element(self, locator):
		self._execute_with_wait(ec.presence_of_element_located((locator.l_type, locator.selector)))

	def long_wait_for_element(self, locator):
		self._execute_with_long_wait(ec.presence_of_element_located((locator.l_type, locator.selector)))

	def count_all_elements(self, locator):
		return len(self.driver.find_elements(locator.l_type, locator.selector))

	def get_all_elements(self, locator):
		return self.driver.find_elements(locator.l_type, locator.selector)

	def get_elements_inside(self, parent_locator, children_locator):
		return self.driver.find_element(parent_locator.l_type, parent_locator.selector).find_elements(
			children_locator.l_type, children_locator.selector)

	def get_elements_inside_element(self, parent_element, children_locator):
		return parent_element.find_elements(children_locator.l_type, children_locator.selector)

	def get_element_inside_element(self, parent_element, children_locator):
		return parent_element.find_element(children_locator.l_type, children_locator.selector)

	def element_exists(self, locator):
		try:
			self._execute_with_wait(ec.presence_of_element_located((locator.l_type, locator.selector)))
			return True
		except TimeoutException:
			return False

	def is_element_visible(self, locator):
		try:
			time.sleep(5)
			self._execute_with_wait(ec.visibility_of_element_located((locator.l_type, locator.selector)))
			return True
		except TimeoutException:
			return False

	def get_element(self, locator, text=""):
		if "ObjectToken" in locator.selector:
			locator.selector = locator.selector.replace("ObjectToken", RunTimeValue)
		isExist = self.element_exists(locator)
		if not isExist:
			raise NoSuchElementException("Could not find ->" + locator.selector)
		return self.driver.find_element(locator.l_type, locator.selector)

	def get_window_size(self):
		return self.driver.get_window_size()

	def swipe(self, start_x, start_y, end_x, end_y, duration=600):
		action = TouchAction(self.driver)
		# It is compulsory to add duration here, otherwise it will not display in the avd emulator
		action.press(x=start_x, y=start_y).wait(duration).move_to(x=end_x, y=end_y).release()
		action.perform()

	def scroll(self, direction="Down", distance=0.8):
		window_size = self.get_window_size()
		midpoint_x = window_size['width'] * 0.5
		midpoint_y = window_size['height'] * 0.5
		top = midpoint_y - window_size['height'] * distance * 0.5
		bottom = midpoint_y + window_size['height'] * distance * 0.5
		left = midpoint_x - window_size['width'] * distance * 0.5
		right = midpoint_x + window_size['width'] * distance * 0.5
		if direction == "Up":
			self.swipe(midpoint_x, top, midpoint_x, bottom)
		elif direction == "Down":
			self.swipe(midpoint_x, bottom, midpoint_x, top)
		elif direction == "Left":
			self.swipe(left, midpoint_y, right, midpoint_y)
		elif direction == "Right":
			self.swipe(right, midpoint_y, left, midpoint_y)

	def tap_in_element(self, element):
		rect = element.rect
		midpoint_x = rect['x'] + rect['width'] * 0.5
		midpoint_y = rect['y'] + rect['height'] * 0.5
		self.driver.execute_script('mobile:tap', {'x': midpoint_x, 'y': midpoint_y, 'element': element})

	def scroll_in_element(self, element, direction="Right", distance=0.8):
		rect = element.rect
		midpoint_x = rect['x'] + rect['width'] * 0.5
		midpoint_y = rect['y'] + rect['height'] * 0.5
		top = midpoint_y - rect['height'] * distance * 0.5
		bottom = midpoint_y + rect['height'] * distance * 0.5
		left = midpoint_x - rect['width'] * distance * 0.5
		right = midpoint_x + rect['width'] * distance * 0.5
		if direction == "Up":
			self.swipe(midpoint_x, top, midpoint_x, bottom)
		elif direction == "Down":
			self.swipe(midpoint_x, bottom, midpoint_x, top)
		elif direction == "Left":
			self.swipe(left, midpoint_y, right, midpoint_y)
		elif direction == "Right":
			self.swipe(right, midpoint_y, left, midpoint_y)

	def scroll_ios(self):
		self.driver.execute_script('mobile: scroll', {'direction': 'down'})

	def scroll_to_element_ios(self, predicate):
		self.driver.execute_script('mobile: scroll', {'direction': 'down', 'predicateString': predicate})

	def get_element_text(self, locator):
		if "ObjectToken" in locator.selector:
			locator.selector = locator.selector.replace("ObjectToken", RunTimeValue)
		if not self.element_exists(locator):
			raise NoSuchElementException("Could not find {locator.selector}")

		self.driver.find_element(locator.l_type, locator.selector).text

	def get_dynamic_text_from_element(self, locator, text):
		global RunTimeValue
		RunTimeValue = text
		dynamic_text = self.get_element(locator, text).text
		locator.selector = re.sub(r"'[A-Z _/a-z]+'", "'ObjectToken'", locator.selector)
		return dynamic_text

	def wait_for_page_load(self):
		page_state = self.driver.execute_script('return document.readyState;')
		return WebDriverWait(self.driver,40).until(page_state == 'complete')


	def enter_text_in_dynamic_field(self, locator, text_to_locate_element, text_to_enter):
		global RunTimeValue
		RunTimeValue = text_to_locate_element
		self.get_element(locator).send_keys(text_to_enter)
		# locator.selector = locator.get_original_selector()

	def multi_select_for_dynamic_element(self, main_element, option_to_select):
		ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(
			"//div[text()='" + main_element + "']/following-siblisng::div//li//span[contains(text(),'" +
			option_to_select + "')]")).click().perform()

	def move_slide_bar(self, element, distance):
		rect = element.rect
		start_x = rect['x']
		end_y = rect['width']
		position = rect['y']
		action = TouchAction(self.driver)
		action.press(x=start_x, y=position).wait(600).move_to(x=end_y * distance, y=position).release()

	def perform_action_on_element(self, locator, action: str, text="", text_to_enter=""):
		try:
			global RunTimeValue
			flag = False
			RunTimeValue = text
			action = action.lower()
			if "ObjectToken" in locator.selector:
				flag = True
			if action == "click":
				self.get_element(locator).click()
			elif action == "dblclick":
				self.get_element(locator).click()
				time.sleep(1)
				self.get_element(locator).click()
			elif action == "get_text":
				value = self.get_element_text(locator)
				# locator.selector = locator.get_original_selector()
				return value
			elif action == "execute_script_click":
				self.driver.execute_script("arguments[0].click();", self.get_element(locator))
			elif action == "type":
				self.get_element(locator).send_keys(text)
			elif action == "type_with_generic_locator":
				self.get_element(locator).send_keys(text_to_enter)
			elif action == "clear":
				self.get_element(locator).clear()
			elif action == "ctra_delete":
				ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').perform()
				ActionChains(self.driver).send_keys(Keys.DELETE).perform()
			elif action == "clickwithactionclass":
				ActionChains(self.driver).move_to_element(self.get_element(locator)).click().perform()
			# elif action == "long-press":
			#     ActionChains(self.driver).longPress(self.get_element(locator)).release().perform()
			elif action == "scroll":
				self.driver.execute_script("arguments[0].scrollIntoView(true)", self.get_element(locator))
			elif action == "scroll_into_middle":
				view_port_height = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
				element_top = "var elementTop = arguments[0].getBoundingClientRect().top;"
				js_function = "window.scrollBy(0, elementTop-(viewPortHeight/2));"
				scroll_into_middle = view_port_height + element_top + js_function
				self.driver.execute_script(scroll_into_middle, self.get_element(locator))
			elif "switch_tab" == action:
				ActionChains(self.driver).key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(
					Keys.CONTROL).perform()
			elif action == "press_enter":
				ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
			elif action == "press_end":
				ActionChains(self.driver).key_down(Keys.END).key_up(Keys.END).perform()
			elif action == "present":
				try:
					assert self.get_element(locator).is_displayed()
				except:
					print(text + " -> Element is not displayed on the page")
					assert False, text + " Element is not displayed on the page"
			elif action == "not_present":
				if self.count_all_elements(locator) == 0:
					assert True, "User does not have access to current action. PASSED"
				else:
					assert False, text + " Element is displayed on the page which is invalid in this case. FAILED"
			elif action == "not_display":
				if "ObjectToken" in locator.selector:
					locator.selector = locator.selector.replace("ObjectToken", RunTimeValue)
				number_of_elements = self.driver.find_elements_by_xpath(locator.selector)
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

	def get_random_string(self, length):
		letters = string.ascii_lowercase
		return ''.join(random.choice(letters) for i in range(length))

	def success_print(self, message):
		print(message)
		return True

	def assert_equal(self, actual, expected, error_message=None, success_message=None):
		error_message = "Assertion Failed : Actual value : " + str(actual) + " , Expected Value : " + str(
			expected) + ", Error Message : " + str(error_message)
		success_message = "Assertion Passed : Actual value : " + str(actual) + " , Expected Value : " + str(
			expected) + ", Success Message : " + str(success_message)
		assert actual == expected and self.success_print(success_message), error_message

	def assert_not_equal(self, actual, expected, error_message=None, success_message=None):
		error_message = "Assertion Failed : Actual value : " + str(actual) + " , Expected Value : " + str(
			expected) + ", Error Message : " + str(error_message)
		success_message = "Assertion Passed : Actual value : " + str(actual) + " , Expected Value : " + str(
			expected) + ", Success Message : " + str(success_message)
		assert actual != expected and self.success_print(success_message), error_message

	def app_active(self):

		self.driver.activate_app('')
