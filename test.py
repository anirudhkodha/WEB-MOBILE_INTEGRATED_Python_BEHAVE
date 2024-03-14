import json
import os.path

from Test_capabilities.ios_caps import ios_bs_caps
from Test_capabilities.ios_caps import environments
# import os
# from Test_capabilities.android_caps import android_bs_caps, environments
#
# #
# #
# capabilities = ios_bs_caps
# #
# TASK_ID = iter([0, 1, 2])
# TASK_ID = TASK_ID.__next__()
# TASK_ID = int(TASK_ID)
# capabilities["deviceName"] = environments[TASK_ID]["deviceName"]
# capabilities["platformVersion"] = environments[TASK_ID]["platformVersion"]
#
# # print(capabilities)
# capabilities = ios_bs_caps
#
# TASK_ID = [0, 1, 2]
# task_id = TASK_ID
#
# if task_id == 0:
# 	capabilities["deviceName"] = environments[TASK_ID]["deviceName"]
# 	capabilities["platformVersion"] = environments[TASK_ID]["platformVersion"]
# 	print(capabilities)

# if task_id == 1:
# 	capabilities["deviceName"] = environments[TASK_ID.__next__()]["deviceName"]
# 	capabilities["platformVersion"] = environments[TASK_ID.__next__()]["platformVersion"]
# 	print(capabilities)
#
# if task_id == 2:
# 	capabilities["deviceName"] = environments[next(TASK_ID)]["deviceName"]
# 	capabilities["platformVersion"] = environments[next(TASK_ID)]["platformVersion"]
# 	print(capabilities)

# -----------------------------------------------------------------------------------------------------------------------

# with open('Test_capabilities/android_caps.py') as config_file:
# 		CONFIG = json.dumps(config_file)
#
# print(CONFIG)






from datetime import datetime, timedelta

#
# future_date = datetime.today() + timedelta(days=4)
#
# # Format the date
# formatted_date = future_date.strftime("%d %b")
#
# # Print the formatted date
# print(formatted_date)


#********	OS	Pre-loaded media file path	Pre-loaded media file names		*********#

# Android	Images:
# /sdcard/Pictures
#
# Images:
# Android_O.png , BrowserStack.jpg , Laptop_with_code.jpg , Test_on_Real_Devices.jpg , UC_Browser_on_iOS.png , s8-tweet.jpg
#
# Videos:
# /sdcard/Movies
#
# Videos:
# android-oreo.mp4 , ipx.mp4 , note_8_on_app_live_tweet.mp4
#
# iOS	Images:
# /private/var/mobile/Media/DCIM/
#
# Images:
# IMG_0001.PNG , IMG_0002.JPG , IMG_0003.PNG , IMG_0004.JPG , IMG_0005.JPG
#
# Videos:
# /private/var/mobile/Media/DCIM/
# Videos:
# IMG_0007.MOV , IMG_0008.MOV , IMG_0009.MOV





# APPIUM_ACTIV_AUTOMATE: sk.eyJ1Ijoid2FyaWRpc2xhbSIsImEiOiJjbGptcHVvNnUxMHd6M2ZsNTExdHhhM2FiIn0.lRUNgWlQJXPGpxC9chfF4A  [TOKEN MAPBOX]