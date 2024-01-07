import sched
import time
from task import task, TASK_FREQUENCY, TASK_PRIORITY


def repeat_task(scheduler, current_time, counter):
    print(scheduler.queue)
    scheduler.enterabs(
        current_time,
        TASK_PRIORITY,
        task,
        argument=(counter,)
    )
    scheduler.enterabs(
        current_time,
        TASK_PRIORITY,
        repeat_task,
        argument=(scheduler, current_time + TASK_FREQUENCY, counter + 1,)
    )


def main():    
    current_time = round(time.monotonic())

    scheduler = sched.scheduler(time.monotonic, time.sleep)
    
    repeat_task(
        scheduler, 
        current_time, 
        0
    )

    scheduler.run()


if __name__ == "__main__":
    main()

