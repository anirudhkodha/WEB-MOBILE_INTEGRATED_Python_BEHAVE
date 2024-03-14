# import os

# app = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Activ_Latest.apk")
# Use Appium-Python-Client v0.27 or above


android_bs_caps = {
	"platformName" : "android",
	"app" : "bs://f89615ec752cbc0b18b5599754cd31407a79609b",
	"automationName": "UiAutomator2 ",
	"autoGrantPermissions ": "true",
	"autoWebview": "true",
	'bstack:options':{
		"projectName" : "ACTIV AUTOMATION",
		"buildName" : "BS",
		"sessionName" : "DEMO",
		"appiumVersion" : "2.0.0",
		"automationVersion" : "latest",
		"debug" : "true",
		"gpsLocation" : "-33.867760303555954,151.2068762673033",
		"timezone" : "Sydney",
		# "geoLocation" : "Au",
		"userName" : "waridislam_DCH20O",
		"accessKey" : "vG5SNwJov3B4X8x5t49V",
		"deviceLogs": "true",
		"networkLogs": "true",
		"idleTimeout": "120",
		# "maskCommands": "setValues",
		"interactiveDebugging": "true",






	},
}

environments = {
		"deviceName": "Google Pixel 6 Pro",
		"platformVersion": "12.0"
		}




	# {
	# "deviceName": "Galaxy S9",
	# "platformVersion": "8.0"
	# },
	# {
	# "deviceName": "Pixel 3 XL",
	# "platformVersion": "9.0"
	# }
	# ]




android_localrun_caps = {

    "platformName": "Android",
    "udid": "emulator-5554",
    "automationName": "UiAutomator2",
	"deviceName": "emulator-5554",
	"appPackage": "au.com.emerg.uat.bartrfs",
    "autoGrantPermissions": "true",
    "uiautomator2ServerInstallTimeout": "80000",
    "appWaitActivity": "*",
    # "chromeOptions": {"w3c": False},
    "nativeWebScreenshot": "true",
    "ignoreHiddenApiPolicyError": "true",
    "adbExecTimeout": "50000",
    "enableWebviewDetailsCollection": "true",
    "autoWebviewTimeout": 4000,
    "recreateChromeDriverSessions": "true"


}
