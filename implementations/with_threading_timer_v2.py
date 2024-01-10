import time, threading
from task import task, TASK_FREQUENCY


def main():
    
    counter = 0
    start_time = time.monotonic()

    print("* Starting task ...")
    
    while True:
        timer = threading.Timer(
            TASK_FREQUENCY - time.monotonic() + start_time + counter, 
            task, 
            args=(counter,)
        )
        timer.start()
        counter += 1

    print("* Finished task")


if __name__ == "__main__":
    main()

