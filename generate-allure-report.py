import subprocess

allure_android_results_path = './allure-results-android'
allure_android_results_dest_path = 'Downloads/ACTIV-allure-results/allure-results-android'
allure_ios_results_path = './allure-results-ios'
allure_ios_results_dest_path = 'Downloads/ACTIV-allure-results/allure-results-ios'
allure_results_dest_path = 'Downloads/ACTIV-automation-allure-results'
allure_report_path = 'Downloads/ACTIV-automation-allure-report'
copy_android_allure_results_cmd = ['cp', '-a', allure_android_results_path, allure_results_dest_path]
copy_ios_allure_results_cmd = ['cp', '-a', allure_ios_results_path, allure_results_dest_path]
date_cmd = 'date +%F-%H%M%S'

# generate a new report number
output = subprocess.check_output(['ls', allure_results_dest_path])
file_list = output.split('\n'.encode())
target_file = file_list[-2]
target_file_string = target_file.decode('utf-8')
max_report_num = target_file_string[0]
next_report_num = int(max_report_num) + 1
print("Next Report Number generated")

# Copy android allurvds""e results
print("Copy android allure results")
subprocess.call(copy_android_allure_results_cmd)

# Copy ios allure results
print("Copy ios allure results")
subprocess.call(copy_ios_allure_results_cmd)
renamed_android_allure_results_path = allure_results_dest_path + '/' + str(next_report_num) + '-android-allure-results'
renamed_ios_allure_results_path = allure_results_dest_path + '/' + str(next_report_num) + '-ios-allure-results'
print("Rename folders")
subprocess.call(['mv', allure_android_results_dest_path, renamed_android_allure_results_path])
subprocess.call(['mv', allure_ios_results_dest_path, renamed_ios_allure_results_path])

# Copy history folder of previous allure report to the allure results folder
print("copy allure report history file")
ls = subprocess.Popen(['ls', allure_report_path],
                      stdout=subprocess.PIPE,
                      )

ios_grep = subprocess.Popen(['grep', 'ios'],
                            stdin=ls.stdout,
                            stdout=subprocess.PIPE,
                            )

ios_tail = subprocess.Popen(['tail', '-n', '1'],
                            stdin=ios_grep.stdout,
                            stdout=subprocess.PIPE,
                            )

ios_end_of_pipe = ios_tail.stdout
ios_targer_report_folder = ''
for line in ios_end_of_pipe:
    line = line.split('\n'.encode())[0]
    ios_targer_report_folder = line.decode('utf-8')
print('ios target report folder: ' + ios_targer_report_folder)
ios_history_folder = allure_report_path + '/' + ios_targer_report_folder + '/history'
print('ios history folder: ' + ios_history_folder)
subprocess.call(['cp', '-a', ios_history_folder, renamed_ios_allure_results_path])

android_ls = subprocess.Popen(['ls', allure_report_path],
                              stdout=subprocess.PIPE,
                              )

android_grep = subprocess.Popen(['grep', 'android'],
                                stdin=android_ls.stdout,
                                stdout=subprocess.PIPE,
                                )

android_tail = subprocess.Popen(['tail', '-n', '1'],
                                stdin=android_grep.stdout,
                                stdout=subprocess.PIPE,
                                )

android_end_of_pipe = android_tail.stdout
android_target_report_folder = ''
for line in android_end_of_pipe:
    line = line.split('\n'.encode())[0]
    android_target_report_folder = line.decode('utf-8')
print('android target report folder: ' + android_target_report_folder)
android_history_folder = allure_report_path + '/' + android_target_report_folder + '/history'
print('android history folder: ' + android_history_folder)
subprocess.call(['cp', '-a', android_history_folder, renamed_android_allure_results_path])

# Generate allure report
print("Generate Allure Report")
datetime_output = subprocess.check_output([date_cmd], shell=True)
datetime_output = datetime_output.split('\n'.encode())[0]
datetime_output = datetime_output.decode('utf-8')
allure_report_android_path = allure_report_path + '/' + datetime_output + '-android-allure-report'
allure_report_ios_path = allure_report_path + '/' + datetime_output + '-ios-allure-report'
subprocess.call(['allure', 'generate', renamed_ios_allure_results_path, '-o', allure_report_ios_path])
print("Script Executed")
