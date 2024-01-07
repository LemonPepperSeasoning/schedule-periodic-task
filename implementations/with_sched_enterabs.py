import sched, time
from task import task, TASK_FREQUENCY, TASK_PRIORITY


def main():
    s = sched.scheduler(time.monotonic, time.sleep)
        
    current_time = round(time.monotonic())
    for i in range(0, 10, TASK_FREQUENCY):
        s.enterabs(
            current_time+i, # with delay 1~10 
            TASK_PRIORITY,
            task,
            argument=(i,)
        )

    print("* Starting job ...")
    s.run()
    print("* Finished job")


if __name__ == "__main__":
    main()

