import schedule
import time 

def job():
    print(f'{time.time()} - Running job')


#schedule.every().day.at('13:56').do(sched_job)
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(0.1)
