import subprocess

command = 'behave --stage=android -i Member -f allure_behave.formatter:AllureFormatter -o ./allure-results-android'

subprocess.call([command], shell=True)