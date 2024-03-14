import subprocess
from settings.config import script_settings

tags = script_settings['tags']
tags_option = '--tags="'
for index, tag in enumerate(tags):
	tags_option = tags_option + tag
	if index != (len(tags) - 1):
		tags_option += ","
tags_option += '"'

ios_command = 'behave --stage=ios -i Member -f allure_behave.formatter:AllureFormatter -o ./allure-results-ios ' + \
			  tags_option

subprocess.call([ios_command], shell=True)
