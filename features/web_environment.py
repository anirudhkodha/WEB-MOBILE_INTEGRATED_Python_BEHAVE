from behave import fixture, use_fixture
from behave.model import *
from behave.model_core import *
from selenium import webdriver as webdriver

from pages.web.Member_Login_Navigation_page import Login_feature
from settings.config import script_settings

# import datetime

def before_all(context):
	print("TESTING Started")

@fixture
def chrome_browser(context, timeout=120):
	Options = webdriver.ChromeOptions()
	context.Browserdriver = webdriver.Chrome(options=Options)
	context.Browserdriver.get("https://activ.uat.rfs.nsw.gov.au/")


@fixture
def firefox_browser(context, timeout=120):
	context.Browserdriver = webdriver.Firefox()


def before_feature(context, feature, timeout=60):

	if script_settings['activ_web']=='true' and'Chrome' in feature.tags:
		use_fixture(chrome_browser,context)

	if 'Firefox' in feature.tags:
		use_fixture(firefox_browser,context)
		context.Browserdriver.get("https://activ.uat.rfs.nsw.gov.au/")


def before_scenario(context ,scenario):
	print(f"START Scenario {scenario.name}")
	if 'Login' in scenario.tags:
		context.loginPageRfsWeb = Login_feature(context.Browserdriver)
		if script_settings['env'] == 'uat':
			username = script_settings['standard_member']['username_01']
		formatted_user = '"' + username + '"'
		context.execute_steps(u'''
			Given I login to rfs activ with "username" and "password"
			'''.format(username=formatted_user))

def after_scenario(context, scenario):
	time.sleep(5)
	# if scenario.status == Status.passed:
	# 	print('Scenario Successfully Passed')
	# else:
	# 	print('Scenario Do Not Passed')
		# if scenario.status == Status.passed :
		# 	context.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Tests Passed"}}')
		# if scenario.status == Status.failed:
		# 	print(f"Failed Scenario {scenario.name}")
		# 	context.driver.execute_script('browserstack_executor: { "action": "setSessionStatus", "arguments": {"status":"failed","reason": "Tests Failed"}}')

def after_feature(context, feature):
	# context.Browserdriver.quit()
	print(f"END Feature {feature.name}")
