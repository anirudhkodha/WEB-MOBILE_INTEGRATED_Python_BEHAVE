import random

from selenium.webdriver.common.by import By

from baseObjects.baseLocator import Locator
from appium.webdriver.common.appiumby import AppiumBy


class Login_Activ:
	Login_Button_First_Screen = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_login"]')
	Login_Button_Second_Screen = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
	Oauth_Not_Your_Account = Locator(AppiumBy.XPATH, '//android.view.View[@content-desc="Not your account?"]')
	MemberIdInput = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText')
	PasswordInput = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText')
	Login_Button_Second_Screen = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
	Allow_prompt= Locator(AppiumBy.XPATH, ".//android.widget.Button[@text='Allow']")

class Menu_Navigations:
	List_view = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("List View")')
	List_view_image = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_layout_listview"]')
	Quick_view_Text = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Quick View")')
	Quick_view_image = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_layout_quickview"]')
	Menu_icon = Locator(AppiumBy.XPATH, '//*[@resource-id="menu"]')
	Menu_contacts = Locator(AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="sideNavBar"]/android.view.ViewGroup/android.view.ViewGroup[5]')
	Search_contacts_field = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText')
	Contact_name = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Warid Islam")')
	Contact_info_FN = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView[2]')
	Contact_info_LN = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.TextView[2]')
	Contact_info_Email = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.view.ViewGroup/android.widget.TextView[2]')
	Sidebar_settings = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings")')
	Settings_name = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Name")')
	Settings_discussion = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Discussion Notifications")')
	Scrollto_logout_button = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text(\"Log Off\"));')
	Confirm_logout = Locator(AppiumBy.XPATH, '//*[@resource-id="android:id/button2"]')
	Bottomnav_broadcast_tab = Locator(AppiumBy.XPATH, '//*[@resource-id="tab_broadcasts"]')


class Availability_Locators:
	Bottomnav_availability_tab = Locator(AppiumBy.XPATH, '//*[@resource-id="tab_availability"]')
	Title_on_availability_tab = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView')
	# Availability TAB : GROUP SELECTION MENU
	Group_selection_icon = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_avail_group"]')
	Select_foundational_platforms = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Foundational Platforms")')
	Select_people_and_business = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("People & Business South Western")')
	Select_people_and_culture = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("People & Culture")')
	Select_policy_unit = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Policy Unit")')
	Select_all_groups = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("All groups")')

	# Availability TAB : TOP NAV BAR 'SET' MENU
	SET_from_top_nav = Locator(AppiumBy.XPATH, '//*[@resource-id="tab_avail_set"]')
	SET_day_select = Locator(AppiumBy.XPATH, '//*[@resource-id="cell_avail_set_day_2"]')
	SET_clock_bar_from = Locator(AppiumBy.XPATH, '	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[2]')
	SET_clock_bar_to = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[2]')
	SET_time_plus_button = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_avail_set_from_add"]')
	SET_time_minus_button = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_avail_set_to_substract"]')
	SET_status_available = Locator(AppiumBy.XPATH, '//*[@resource-id="row_avail_set_type_0"]')
	Save_availability = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_avail_set_save"]')

	# Availability TAB : TOP NAV BAR 'WEEKLY' MENU
	WEEKLY_from_top_nav = Locator(AppiumBy.XPATH, '//*[@resource-id="tab_avail_weekly"]')


class Broadcast_Locators_Quickview:

	Quickviiew_declined_button = Locator(AppiumBy.XPATH, '//*[@resource-id="cell_msg_0_btn_decline"]')
	Quickviiew_accept_button = Locator(AppiumBy.XPATH, '//*[@resource-id="cell_msg_0_btn_accept"]')
	Quickviiew_attendance_button = Locator(AppiumBy.XPATH, '//*[@resource-id="cell_msg_0_btn_attendance"]')
	Quickviiew_options_button = Locator(AppiumBy.XPATH, '//*[@resource-id="cell_msg_0_btn_opts"]')



class Broadcast_Group_Listview:
	Attendance_Member_details = None
	Recent_Broadcast_Tile = Locator(AppiumBy.XPATH, '//*[@resource-id="row_msg_0"]')
	Accept_button = Locator(AppiumBy.XPATH, '//*[@resource-id="row_msg_0_btn_attend"]')
	Decline_button = Locator(AppiumBy.XPATH, '//*[@resource-id="row_msg_0_btn_decline"]')
	Other_button = Locator(AppiumBy.XPATH, '//*[@resource-id="row_msg_0_btn_other"]')
	Options_button = Locator(AppiumBy.XPATH, '//*[@resource-id="row_msg_0_btn_opts"]')
	Options_button = Locator(AppiumBy.XPATH, '//*[@resource-id="row_msg_0_btn_opts"]')
	Map_button = Locator(AppiumBy.XPATH, '//*[@resource-id="row_msg_0_btn_map"]')
	Attendance_Logged = Locator(AppiumBy.XPATH, '//android.widget.TextView[@text="Attendance Logged"]')
	Attending = Locator(AppiumBy.ANDROID_UIAUTOMATOR, "new Uiselector.resourceIdMatches('row_attend_')")
	Attendance_name = Locator(AppiumBy.XPATH, '//android.widget.TextView[@text="Warid Islam"]')
	Attendance_phone = Locator(AppiumBy.XPATH, '//android.widget.TextView[@text="0405019666"]')
	# Attendance_details = [Attendance_name, Attendance_phone]                                                                                                              qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq


class ListView_PlusButton_Broadcast_Locators:
	Bottomnav_broadcasts_tab = Locator(AppiumBy.XPATH, '//*[@resource-id="tab_broadcasts"]')
	Listview_plus_button = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_plus_opts"]')
	Listview_plus_button_broadcast = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_plus_bcast"]')
	Listview_plus_button_broadcast_to = Locator(AppiumBy.XPATH, '//*[@resource-id="row_newbcast_Capcode"]')
	Listview_plus_button_broadcast_to_Select = AppiumBy.XPATH, '//*[@resource-id="row_listpicker_Capcode_0"]'
	# Navigate back to broadcast
	Listview_plus_button_broadcast_to_seleected = Locator(AppiumBy.XPATH, '//*[@text="ACTIV BRG Foundational Platforms"]') #For text assert
	ListView_plus_button_broadcast_Location = Locator(AppiumBy.XPATH, '//*[@resource-id="row_newbcast_LatLng"]')
	ListView_plus_button_broadcast_Location_search = Locator(AppiumBy.CLASS_NAME, 'android.widget.EditText')
	Location_popup_allow = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("While using the app")')
	Location_search = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("PENRITH")')
	ListView_plus_button_broadcast_Location_Select = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Penrith, NSW").className("android.widget.TextView")')
	Coord_bradcast = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.EditText')
	Add = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add")')
	Location_confirm = Locator(AppiumBy.XPATH, '//*[@resource-id="row_newbcast_LatLng"]/android.view.ViewGroup/android.widget.TextView'[2])
	Attachment = Locator(AppiumBy.XPATH, '//*[@resource-id="row_newbcast_Attachment"]')
	upload_image = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Upload Image")')
	upload_image_folders = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pictures")')
	image_select = Locator(AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="Photo taken on Jul 12, 2023 01:23:50"])[1]')
	Alert = Locator(AppiumBy.XPATH, '//*[@resource-id="swch_newbcast_Alert"]')
	Alert_confirm = 'ON'
	Broadcast_Message = Locator(AppiumBy.CLASS_NAME,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText')
	random_number = str(random.randint(1, 100))
	Broadcast_name = ("Automated test_broadcast"+random_number)
	Broadcast_Send = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_newbcast_send"]')

class Maps:
	Map_prompts_allow = Locator(AppiumBy.XPATH, '//*[@resource-id=com.android.permissioncontroller:id/permission_allow_foreground_only_button"]')
	My_Loc_icon = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_map_myloc"]')
	Map_All = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_map_all"]')
	Map_water = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_map_water"]')
	Map_direction = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_map_direction"]')
	Map_refresh = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_map_refresh"]')
	Map_zoom = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_map_zoom"]')
	Map_options = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_map_options"]')
	Map_layers = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_map_layers"]')
	Map_cord_next = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_map_cord_next"]')
	Map_cord_prev = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_map_cord_prev"]')
	My_Location_text = Locator(AppiumBy.XPATH, '//android.widget.TextView[@text="My Location"]')
	Map_elements_all = [My_Loc_icon, Map_All, Map_water, Map_direction, Map_refresh, Map_zoom, Map_options, Map_layers, Map_cord_next, Map_cord_prev, My_Location_text]
	Distance = Locator(AppiumBy.XPATH, '//android.widget.TextView[@text="DISTANCE"]/android.widget.TextView')
	ETA = Locator(AppiumBy.XPATH, '//android.widget.TextView[@text="ETA"]/android:widget.TextView')

class Alert_Actions:
	Assign_team = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_alert_assign"]')