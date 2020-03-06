
from apscheduler.schedulers.blocking import BlockingScheduler
from server import list_paths # run_covidify

sched = BlockingScheduler()

'''
This is will the function in app.py that dow
'''
@sched.scheduled_job('cron', day_of_week='0-6', hour='0-23', minute='0-59/1', timezone='America/New_York')
def run_example():
    # run_covidify()
    list_paths()

sched.start()
