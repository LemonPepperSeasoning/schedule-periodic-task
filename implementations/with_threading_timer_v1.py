import time, threading
from task import task, TASK_FREQUENCY


def main():
    
    print("* Starting task ...")
    
    for i in range(0, 10, TASK_FREQUENCY):
        timer = threading.Timer(i, task, args=(i,))
        timer.start()

    print("* Finished task")


if __name__ == "__main__":
    main()

