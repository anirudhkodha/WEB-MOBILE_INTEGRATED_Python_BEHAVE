import subprocess

from settings.config import script_settings

assert isinstance(script_settings, object)

tags = script_settings['tags']
tags_option = '--tags="'
for index, tag in enumerate(tags):
	tags_option = tags_option + tag
	if index != (len(tags) - 1):
		tags_option += ","
tags_option += '"'

android_command = 'behave --stage=android -i Member -f allure_behave.formatter:AllureFormatter -o ./allure-results-android ' + tags_option

subprocess.call([android_command], shell=True)
