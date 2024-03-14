import subprocess
from settings.config import script_settings

tags = script_settings['tags']
tags_option='--tags=" '
for index, tag in enumerate(tags):
    tags_option=tags_option + tag
    if index != (len(tags) - 1):
        tags_option += ","
tags_option += '"'

# ios_command = 'behave --stage=ios -i Member -f allure_behave.formatter:AllureFormatter -o ./allure-results-ios ' + tags_option
# android_command = 'behave --stage=android -i Member -f allure_behave.formatter:AllureFormatter -o ./allure-results-android ' + tags_option
# commands = ios_command + '\n' + android_command
# print(commands)
#
# for process in [subprocess.Popen(['/bin/bash', '-c', line], stdout=subprocess.PIPE)
#                 for line in commands.split("\n") if line]:  # filter out blank lines
#     out, err = process.communicate()
#     # print out & err
#
# print(out)
