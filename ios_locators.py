from baseObjects.baseLocator import Locator
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By



#                                                          << LOGIN_LOGOUT >>


class Login_Logout_Activ:
	Login_Button_First_Screen = Locator(By.NAME, 'btn_login')
	Login_Button_Second_Screen = Locator(By.NAME, 'Log In')

	Oauth_Not_Your_Account = Locator(AppiumBy.IOS_PREDICATE,'label == "Not your account?" AND name == "Not your account?" AND value == "Not your account?"')

	MemberIdInput = Locator(AppiumBy.IOS_PREDICATE,'label == "User name"')
	PasswordInput = Locator(AppiumBy.IOS_PREDICATE,'label == "Password"')



class Event_Tab_Locators:
	Bottomnav_event_tab = Locator(AppiumBy.NAME, "tab_events")
	Event_tab_title = Locator(AppiumBy.NAME, "Events")
	Event_tab_listview_btn_ontop = Locator(AppiumBy.NAME, "btn_event_calview")
	Event_tab_addnew_btn_ontop	= Locator(AppiumBy.NAME, "btn_event_add")
	Event_tab_addnew_EvtName = Locator(AppiumBy.NAME, "txt_edit_event_Name")
	Event_tab_addnew_grpname = Locator(AppiumBy.NAME, "row_edit_event_AccessKey")
	Event_tab_addnew_grpname_select = Locator(AppiumBy.NAME, 'row_listpicker_AccessKey_1')
	Event_tab_addnew_to = Locator(AppiumBy.NAME, "row_edit_event_Capcode")
	Event_tab_addnew_to_select = Locator(AppiumBy.NAME, "row_listpicker_Capcode_1")
	Event_tab_addnew_type = Locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="row_edit_event_EventTypeId"]')
	Event_tab_addnew_type_select = Locator(AppiumBy.NAME, 'row_listpicker_EventTypeId_24')
	Event_tab_addnew_status = Locator(AppiumBy.NAME, "row_edit_event_EventStatusId")
	Event_tab_addnew_Resources = Locator(AppiumBy.NAME, "row_edit_event_ResourceId")
	Event_tab_addnew_Resources_select = Locator(AppiumBy.IOS_PREDICATE, 'label == "RUPESH 3" AND name == "row_listpicker_ResourceId_0"')
	Event_tab_addnew_Start = Locator(AppiumBy.NAME, "row_edit_event_StartDate")
	Event_tab_addnew_end= Locator(AppiumBy.NAME, "row_edit_event_EndDate")
	Event_tab_addnew_broadcast= Locator(AppiumBy.NAME, "row_edit_event_BroadcastDate")
	Event_tab_addnew_repeat= Locator(AppiumBy.NAME, "row_edit_event_undefined")
	Event_tab_addnew_location= Locator(AppiumBy.NAME, "row_edit_event_Location")
	Event_tab_addnew_location_Search = Locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Search..."]/XCUIElementTypeTextField')
	Event_tab_addnew_location_select = Locator(AppiumBy.NAME, "Town Hall, NSW")
	Event_tab_addnew_location_add = Locator(AppiumBy.NAME, "Add")
	Event_tab_addnew_MinMembers= Locator(AppiumBy.IOS_PREDICATE, 'label == "Min Members " AND name == "row_edit_event_MinLimit"')
	Event_tab_addnew_MaxMembers= Locator(AppiumBy.NAME, 'label == "Max Members " AND name == "row_edit_event_MaxLimit"')
	Event_tab_addnew_RSVP= Locator(AppiumBy.ACCESSIBILITY_ID, "row_edit_event_RSVPDate")
	Event_tab_addnew_notes= Locator(AppiumBy.NAME, "txt_edit_event_Notes")
	Event_tab_addnew_Reminder= Locator(AppiumBy.NAME, "row_edit_event_ReminderDate")

	Event_tab_DATE  = Locator(AppiumBy.XPATH, "//XCUIElementTypePickerWheel")

	EVENT_date_parent_element = Locator(AppiumBy.XPATH, "//XCUIElementTypeDatePicker/XCUIElementTypePicker/XCUIElementTypePickerWheel[1]")
	EVENT_hour_element = Locator(AppiumBy.XPATH, "//XCUIElementTypeDatePicker/XCUIElementTypePicker/XCUIElementTypePickerWheel[2]")
	Event_minute_element = Locator(AppiumBy.XPATH, "//XCUIElementTypeDatePicker/XCUIElementTypePicker/XCUIElementTypePickerWheel[3]")

	Selected_Min_Members = Locator(AppiumBy.XPATH, '//XCUIElementTypePicker[@name="picker_number"]/XCUIElementTypePickerWheel')
	Selected_Max_Members = Locator(AppiumBy.XPATH, '//XCUIElementTypePicker[@name="picker_number"]/XCUIElementTypePickerWheel')

	RSVP_date_parent_element = Locator(AppiumBy.XPATH, "//XCUIElementTypeDatePicker/XCUIElementTypePicker/XCUIElementTypePickerWheel[1]")
	RSVP_hour_element = Locator(AppiumBy.XPATH, "//XCUIElementTypeDatePicker/XCUIElementTypePicker/XCUIElementTypePickerWheel[2]")
	RSVP_minute_element = Locator(AppiumBy.XPATH, "//XCUIElementTypeDatePicker/XCUIElementTypePicker/XCUIElementTypePickerWheel[3]")

	Event_save = Locator(AppiumBy.IOS_PREDICATE, 'label == "Save"')
	Location_popup_allow = Locator(AppiumBy.NAME, "Allow While Using App")





class Availability_Locators:

	Bottomnav_availability_tab = Locator(AppiumBy.XPATH, '//*[@resource-id="tab_availability"]')
	Title_on_availability_tab = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView')


#                                      << * Availability TAB : TOP NAV BAR 'GROUP' MENU * >>



	Group_selection_icon = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_avail_group"]')
	Select_foundational_platforms = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Foundational Platforms")')
	Select_people_and_business = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("People & Business South Western")')
	Select_people_and_culture = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("People & Culture")')
	Select_policy_unit = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Policy Unit")')
	Select_all_groups = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("All groups")')


#                                     << * Availability TAB : TOP NAV BAR 'SET' MENU * >>

	SET_from_top_nav = Locator(AppiumBy.XPATH, '//*[@resource-id="tab_avail_set"]')
	SET_day_select = Locator(AppiumBy.XPATH, '//*[@resource-id="cell_avail_set_day_2"]')
	SET_clock_bar_from = Locator(AppiumBy.XPATH, '	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[2]')
	SET_clock_bar_to = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[2]')
	SET_time_plus_button = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_avail_set_from_add"]')
	SET_time_minus_button = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_avail_set_to_substract"]')
	SET_status_available = Locator(AppiumBy.XPATH, '//*[@resource-id="row_avail_set_type_0"]')
	Save_availability = Locator(AppiumBy.XPATH, '//*[@resource-id="btn_avail_set_save"]')

#                                      << * Availability TAB : TOP NAV BAR 'WEEKLY' MENU  * >>

	WEEKLY_from_top_nav = Locator(AppiumBy.XPATH, '//*[@resource-id="tab_avail_weekly"]')






#                              << BROADCAST_TAB :: Event Components>>
class Broadcast_Tab_QuickView:
	Bottomnav_broadcast_tab = Locator(AppiumBy.NAME , 'tab_broadcasts')
	Quickview_eventdetails_title = Locator(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name BEGINSWITH "ACTIV BRG"')
	Quickview_event_ref_value = Locator(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name ENDSWITH "_ref"')
	Quickview_event_create_date = Locator(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name ENDSWITH "_created"')
	Quickview_event_group = Locator(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name ENDSWITH "_group"')
	Quickviiew_declined_button = Locator(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name CONTAINS "_btn_decline"')
	Quickviiew_accept_button = Locator(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name CONTAINS "_btn_attend"')
	Quickviiew_other_button = Locator(AppiumBy.IOS_PREDICATE,'type == "XCUIElementTypeOther" AND name CONTAINS "_btn_other"')
	Quickviiew_attendance_button = Locator(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name ENDSWITH "_btn_attendance"')
	Quickviiew_options_button = Locator(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name ENDSWITH "_btn_opts"')
	Quickviiew_options_button_Copy = Locator(AppiumBy.IOS_PREDICATE, 'label == "Copy"')
	Quickviiew_options_button_Forward = Locator(AppiumBy.IOS_PREDICATE, 'label == "Forward"')
	Quickviiew_options_button_AssigntoTeam =  Locator(AppiumBy.IOS_PREDICATE, 'label == "Assign to Team"')
	Quickviiew_options_button_StandDown = Locator(AppiumBy.IOS_PREDICATE, 'label == "Message: Stand Down""')
	Quickviiew_options_button_UpdateLocation = Locator(AppiumBy.IOS_PREDICATE, 'label == "Update Location"')
	Quickview_eventdetails_button = Locator(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name ENDSWITH "_btn_event"')

class Broadcast_Tab_Inside_Event_Attendance:
	Attendance_Page_title = Locator(By.NAME, 'Response')
	Attending = Locator(AppiumBy.IOS_PREDICATE, "name BEGINSWITH 'row_attend_'")








class Menu_Navigations:
# ************************************* <<<<<  Navigation Locators [LAYOUTSCREENS] >>>>> ***************************************************************************************************************

	List_view_layout = Locator(By.NAME, 'btn_layout_listview')
	Quick_view_layout = Locator(By.NAME,'btn_layout_quickview')

# *********************************** <<<<<  HAMBURGER MENU LOCATORS >>>>> **************************************************************************
	Menu_icon = Locator(By.NAME, "menu")
	Menu_contacts_button = Locator(AppiumBy.IOS_PREDICATE, 'label == "Contacts" AND name == "Contacts" AND type == "XCUIElementTypeButton"')
	Menu_documents_button = Locator(AppiumBy.IOS_PREDICATE, 'label == "Documents" AND name == "Documents""')
	Menu_teams_button = Locator(AppiumBy.IOS_PREDICATE, 'label == "Teams" AND name == "Teams"')
	Menu_listview_button = Locator(AppiumBy.IOS_PREDICATE, 'label == "ListView" AND name == "ListView"')
	Menu_quickview_button = Locator(AppiumBy.IOS_PREDICATE, 'label == "QuickView" AND name == "QuickView"')
	Menu_map_button = Locator(AppiumBy.IOS_PREDICATE, 'label == "Map" AND name == "Map"')
	Menu_help_button = Locator(AppiumBy.IOS_PREDICATE, 'label == "Help" AND name == "Help"')
	Menu_settings_button = Locator(AppiumBy.IOS_PREDICATE, 'label == "Settings" AND name == "Settings"')
	Logout_button = Locator(AppiumBy.IOS_PREDICATE, 'label == "Log Off " AND name == "btn_setting_"')
	Confirm_Logout_button = Locator(AppiumBy.NAME, 'name == "Logout"')


	#************************************************************************** <<<<<NED TO BE UPDATED>>>> ***************************************************************************************************************
	# Search_contacts_field = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText')
	# Contact_name = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Warid Islam")')
	# Contact_info_FN = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView[2]')
	# Contact_info_LN = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.TextView[2]')
	# Contact_info_Email = Locator(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.view.ViewGroup/android.widget.TextView[2]')
	# Sidebar_settings = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings")')
	# Settings_name = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Name")')
	# Settings_discussion = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Discussion Notifications")')
	# Scrollto_logout_button = Locator(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text(\"Log Off\"));')
	# Confirm_logout = Locator(AppiumBy.XPATH, '//*[@resource-id="android:id/button2"]')
	#************************************************************************** <<<<<NED TO BE UPDATED>>>> ***************************************************************************************************************




	#********************************************** <<<<<  close opened wondow[Tap on cross] >>>>>**********************************************************************************************************************
	Close_button = Locator(AppiumBy.NAME, 'close')
	#********************************************** <<<<< 									 >>>>>**********************************************************************************************************************