import subprocess

commands = '''
behave --stage=ios -i Member -f allure_behave.formatter:AllureFormatter -o ./allure-results-ios
behave --stage=android -i Member -f allure_behave.formatter:AllureFormatter -o ./allure-results-android
'''

for process in [subprocess.Popen(['/bin/bash', '-c', line], stdout=subprocess.PIPE)
                for line in commands.split("\n") if line]:  # filter out blank lines
    out, err = process.communicate()
    # print out & err
