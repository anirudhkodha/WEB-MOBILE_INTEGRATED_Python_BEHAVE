import builtins
import datetime

import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from behave import fixture, use_fixture
from behave.model import *
from behave.model_core import *
from Test_capabilities.ios_caps import ios_bs_caps, ios_caps_single_run, environments
from pages.ios.Member_Login_Navigation_page import Login_feature
from settings.config import script_settings

def launch_activ_app_if_not_run(context):
	current_view = context.driver.current_context
	if current_view != "NATIVE_APP":
		context.driver.execute_script('mobile: launchApp', {'bundleId': 'au.com.emerg.uat.bartrfs'})

def terminate_app(context):
	context.driver.terminate_app('au.com.emerg.uat.bartrfs')
	time.sleep(2)

def launch_without_ios_app(context):
	context.driver.installApp(os.path.join(os.path.dirname(os.path.abspath(__file__)), ""))

@fixture
def appium_driver(context, timeout=30):

	if script_settings['browserstack_parallel'] == 'true':
		capabilities = dict(ios_bs_caps)

		capabilities["deviceName"] = environments["deviceName"]
		capabilities["platformVersion"] = environments["platformVersion"]
		print(capabilities)

		# if	task_id == 1:
		# 	capabilities["deviceName"] = environments [task_id]["deviceName"]
		# 	capabilities["platformVersion"] = environments [task_id]["platformVersion"]
		# 	print(capabilities)
		#
		# if task_id == 2:
		# 	capabilities["deviceName"] = environments [task_id]["deviceName"]
		# 	capabilities["platformVersion"] = environments [task_id]["platformVersion"]
		# 	print(capabilities)


	context.driver = webdriver.Remote(
		command_executor='http://waridislam_DCH20O:vG5SNwJov3B4X8x5t49V@hub-cloud.browserstack.com/wd/hub',
		desired_capabilities=dict(capabilities)
	)
	context.driver.implicitly_wait(10)

	if script_settings['browserstack_single'] == 'true':
		context.driver = webdriver.Remote(
			command_executor='http://waridislam_DCH20O:vG5SNwJov3B4X8x5t49V@hub-cloud.browserstack.com/wd/hub',
			desired_capabilities=dict(ios_caps_single_run)
		)
	else:
		print("No Driver Initiated")


def before_all(context):
	print("TESTING Started")


def before_feature(context, feature):
	return use_fixture(appium_driver, context)




def before_scenario(context, scenario):
	builtins.print(f"START Scenario {scenario.name}")

	if 'Login' in scenario.tags:
		context.loginPageRfs = Login_feature(context.driver)
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
		allure.attach(context.driver.get_screenshot_as_png(),name=str(datetime.datetime.now().timestamp()),attachment_type=AttachmentType.PNG)

def after_feature(context, driver: webdriver.Remote, feature):

	context.driver.quit()  # (quit the driver after feature is executed)

def after_all(context):
	builtins.print("TESTING COMPLETED")
