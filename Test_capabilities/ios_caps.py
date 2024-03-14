import os

app = os.path.join(os.path.dirname(os.path.abspath(__file__)), "")

ios_caps_single_run = {
    "app": "bs://993f3c5b1f6620f1012148d8ae5d40c83314e5ff",
    "browserstack.user": "waridislam_DCH20O",
    "browserstack.key": "vG5SNwJov3B4X8x5t49V",
    "platformName": "iOS",
    "project": "ACTIV Behave iOS Project",
    "build": "browserstack-build-Single-device",
    "name": "Single_device_test",
    "automationName": "XCUITest",
	"browserstack.appiumVersion" : "2.0.0",
	"browserstack.automationVersion": "latest",
	"browserstack.debug": "true",
	"browserstack.networkLogs": "true",
	"deviceName": "iPhone 14",
    "platformVersion": "16.0",
    "noReset": "true",
    "fullReset": "false",
    "autoAcceptAlerts": "true",
    "chromeOptions": {"w3c": False},
    "locationServicesAuthorized": "true",
    "locationServicesEnabled": "true"
}

ios_bs_caps = {
    "app": "bs://993f3c5b1f6620f1012148d8ae5d40c83314e5ff",
    "browserstack.user": "waridislam_DCH20O",
    "browserstack.key": "vG5SNwJov3B4X8x5t49V",
    "platformName": "iOS",
    "project": "First Behave iOS Project",
    "build": "browserstack-build-1",
    "name": "Parallel_test",
    "automationName": "XCUITest",
    "browserstack.debug": "true",
	"browserstack.appiumVersion" : "2.0.0",
	"browserstack.automationVersion" : "latest",
    "browserstack.networkLogs": "true",
    "autoAcceptAlerts": "true",
    "noReset": "true",
    "fullReset": "false",
    "chromeOptions": {"w3c": False},
    "locationServicesAuthorized": "true",
    "locationServicesEnabled": "true"
	}

environments = [
    {
	"deviceName": "iPhone 14 Pro Max",
	"platformVersion": "16.0"
    },
]
    # {
	# "deviceName": "iPhone 13 Pro Max",
	# "platformVersion": "15.0"
    # },
    # {
	# "deviceName": "iPhone 12 Pro Max",
	# "platformVersion": "14.0"
    # }


ios_home_caps = {
    "app": app,
    "platformName": "iOS",
    "platformVersion": "14.5",
    "deviceName": "iPhone 12 Pro Max",
    "automationName": "XCUITest",
    "noReset": "true",
    "systemPort": "8200",
    "autoAcceptAlerts": "true",
    "chromeOptions": {"w3c": False},
    "locationServicesAuthorized": "true",
    "locationServicesEnabled": "true",
    "bundleId": "au.com.star.mobileapp.digital",
    "includeSafariInWebviews": "true",
    "webviewConnectTimeout": "5000"
}
