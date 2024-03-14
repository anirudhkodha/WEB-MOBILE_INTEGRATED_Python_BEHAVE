import threading
from paver.easy import *
from paver.setuputils import setup
from paver.tasks import *

setup(
    name = "RfsActivAutomation",
    version = "0.1.0",
    author = "Warid Islam",
    author_email = "Warid.Islam@rfs.nsw.gov.au",
    description = ('ACTIV MOBILE Automation With Appium Python-Behave For Both iOS & Android'),
	license= "MIT",
	keywords = "rfs-active-automation",
	url = "https://github.com/NSWRFS/RfsActivAutomation",
    packages = ['features']
)

def run_ios_test(task_id):
		sh(f'TASK_ID=%s & behave --stage=ios -i "features/Member_Event.feature"' % task_id)

def run_android_test(task_id):
		sh(f'set TASK_ID=%s & behave --stage=android -i "features/Member_Broadcast.feature"' % task_id)


@task
@consume_nargs(2)
def run(args):
	if args[0] == 'parallel_tests':
		if args[1] == 'ios':
			jobs = []
			for index in range(1):
				# TASK_ID = iter([0, 1, 2])
				# task_id = TASK_ID.__next__()
				thread = threading.Thread(target=run_ios_test,args=(index,))
				jobs.append(thread)
				thread.start()
			for thread in jobs:
				thread.join()

		if args[1] == 'android':
			jobs = []
			for index in range(1):
				# TASK_ID = iter([0, 1, 2])
				# task_id = TASK_ID.__next__()
				thread = threading.Thread(target=run_android_test,args=(index,))
				jobs.append(thread)
				thread.start()
			for thread in jobs:
				thread.join()
	else:
		print("Wrong pvaer task")