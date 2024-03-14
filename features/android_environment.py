import builtins
import datetime
import time
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from selenium.webdriver.common.by import By
from settings.config import script_settings
from Test_capabilities.android_caps import android_bs_caps, android_localrun_caps, environments
from behave import *
from behave.fixture import fixture
from behave.model_core import *
import pages.android.Member_Login_Navigation_page
# from baseObjects.baseMethods import  BaseMethods
def launch_activ_app_if_not_run(context):
	current_view = context.driver.current_context
	if current_view != "NATIVE_APP":
		context.driver.activate_app('au.com.emerg.uat.bartrfs')


def terminate_app(context):
	context.driver.terminate_app('au.com.emerg.uat.bartrfs')
	time.sleep(2)


def launch_without_android_app(context):
	context.driver.installApp('')

@fixture
def appium_driver(context, timeout=30):

	if script_settings['browserstack_parallel'] == 'true':
		capabilities = dict(android_bs_caps)

		capabilities["deviceName"] = environments["deviceName"]
		capabilities["platformVersion"] = environments["platformVersion"]
		print(capabilities)

		# if task_id == 1:
		# 	capabilities["deviceName"] = environments[task_id]["deviceName"]
		# 	capabilities["platformVersion"] = environments[task_id]["platformVersion"]
		# 	print(capabilities)
		#
		# if task_id == 2:
		# 	capabilities["deviceName"] = environments[task_id]["deviceName"]
		# 	capabilities["platformVersion"] = environments[task_id]["platformVersion"]
		# 	print(capabilities)

		context.driver = webdriver.Remote(
			command_executor='http://waridislam_DCH20O:vG5SNwJov3B4X8x5t49V@hub-cloud.browserstack.com/wd/hub',
			desired_capabilities=dict(capabilities)
		)
		context.driver.implicitly_wait(10)



	if script_settings['android_emulator'] == 'true':
		context.driver = webdriver.Remote(
			command_executor=script_settings['android_port'],
			desired_capabilities=dict(android_localrun_caps))

	else:
		builtins.print("No Driver Initiated")


	# -- AFTER-FEATURE: Cleanup ----------------------------------------
	yield context.driver
	context.driver.quit()


def before_all(context):

	builtins.print("TESTING Started")


def before_feature(context, feature):
	return use_fixture(appium_driver, context)


def before_scenario(context, scenario):
	print(f"START Scenario {scenario.name}")

	if 'Location' in scenario.tags:
		# Open Location settings
		context.driver.start_activity("com.android.settings", "com.android.settings.Settings$LocationSettingsActivity")

		# Toggle Location services
		toggle_button = context.driver.find_element(By.XPATH, "//*[@class = 'android.widget.Switch']")
		toggle_button_state = toggle_button.get_attribute("text")
		if toggle_button_state == "OFF":
			toggle_button.click()

		# Close the settings app
		context.driver.terminate_app('com.android.settings')
		# Activate the app under test
		context.driver.activate_app('au.com.emerg.uat.bartrfs')

	if 'Login' in scenario.tags:
		context.loginPageRfs = pages.android.Member_Login_Navigation_page.Login_feature(context.driver)
		if script_settings['env'] == 'uat':
			username = script_settings['standard_member']['username_01']
		formatted_user = '"' + username + '"'
		context.execute_steps(u'''
			Given I login to rfs activ with "username" and "password"
			'''.format(username=formatted_user))

	if 'Listview' in scenario.tags:
		context.execute_steps(u'''
			Given I click on ListView    
				''')

	if 'Quickview' in scenario.tags:
		context.execute_steps(u'''
			Given I click on QuickView
				''')
	launch_activ_app_if_not_run(context)



def after_scenario(context, scenario):

	if 'Logout' in scenario.tags:
		context.execute_steps(u'''
			Then I logout as a member
				''')

	if scenario.status == Status.passed:
		context.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status": "passed", "reason": "Tests Passed"}}')
	elif scenario.status == Status.failed:
		print(f"Failed Scenario {scenario.name}")
		context.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status": "failed", "reason": "Tests Failed"}}')

def after_step(context, step):
	if step.status == "failed":
		allure.attach(context.driver.get_screenshot_as_png(),
					  name=str(datetime.datetime.now().timestamp()),
					  attachment_type=AttachmentType.PNG,
					  )

def after_feature(context, feature):
	context.driver.quit()



def after_all(context):
	print("TESTING COMPLETED")

# def capture_screenshots_for_jira(context):
#     path = os.getcwd() + "/temp"
#     if os.path.exists(path):
#         shutil.rmtree(path)
#     os.mkdir(path)
#     path_to_capture_screenshot = path + "/" + builtins.str(datetime.datetime.now().timestamp()) + ".png"
#     context.driver.get_screenshot_as_file(path_to_capture_screenshot)
#     return path_to_capture_screenshot
