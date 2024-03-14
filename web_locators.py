from baseObjects.baseLocator import Locator
from selenium.webdriver.common.by import By



class Login_logout_Web:
	Login_Button = Locator(By.ID,'btn-login')
	Login_Button_Auth0 = Locator(By.XPATH,'//*[@name="submit"]')
	MemberIdInput = Locator(By.XPATH, '//*[@name="username"]')
	PasswordInput = Locator(By.XPATH, '//*[@name="password"]')
	LogOut = Locator(By.ID,'log-off')



class Menu_Navigations:

# *********************************** <<<<<  HAMBURGER SIDE MENU LOCATORS >>>>> **************************************************************************
	Menu_sidebar = Locator(By.ID, "sidemenu")
	Menu_Messaging_button = Locator(By.ID,"Broadcasts")
	Menu_Contacts_button = Locator(By.ID,"Contacts" )
	Menu_TeamPlanner_button = Locator(By.ID, "TeamPlanner")
	Menu_Documents_button = Locator(By.ID,"Documents")
	Menu_Teams_button = Locator(By.ID,"Contacts")
	Menu_Events_button = Locator(By.ID,"Events")
	Menu_Availability_button = Locator(By.ID,"Availability")
	Menu_TeamPlanner_button = Locator(By.ID,"TeamPlanner")
	Menu_Dashboard_button = Locator(By.ID,"Groups")
	Menu_MyGroups_button = Locator(By.ID,"Groups")
	Menu_Myprofile_button = Locator(By.ID,"UserSettings")


class Event_Feeds:
	NEW_Button = Locator(By.XPATH, '//*[@id="global-new-button"]')
	Event_List = Locator(By.XPATH, '//*[@id="table-broadcast"]/tbody/tr[1]')
	GRP_OF_EVENT = Locator(By.XPATH, '//*[@id="table-broadcast"]/tbody/tr[1]/td/div[1]/div[1]/div')
	NAME_OF_Event = Locator(By.XPATH, '//*[@id="table-broadcast"]/tbody/tr[1]/td/div[2]/div/div[2]')
	Generate_Report= Locator(By.XPATH, '//*[@id="table-broadcast"]/tbody/tr[1]/td/div[2]/div/div[3]/div[2]/button[1]')
	Downldad_report = Locator(By.ID, 'dowmload')

class Event_action:
	NEW_Button = Locator(By.XPATH, '//*[@id="global-new-button"]')
	NEW_Broadcast = Locator(By.CSS_SELECTOR, '#dropdown-menu-newnotification')
	_Grp_To = Locator(By.CSS_SELECTOR, "#New-Notification-BroadcastTagsDiv")
	_Grp_options = Locator(By.XPATH, '//*[@id="New-Notification-BroadcastTagsDiv"]/span[1]/span/ul/li/input')
	Message_box = Locator(By.XPATH, "//textarea[@id='New-Notification-Textbox']")
