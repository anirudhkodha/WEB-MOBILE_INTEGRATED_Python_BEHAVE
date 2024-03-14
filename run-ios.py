import subprocess

command = 'behave --stage=ios -i Member -f allure_behave.formatter:AllureFormatter -o ./allure-results-ios'

subprocess.call([command], shell=True)
