import sched, time


def job(id=0):
    print(f"{time.time()} - Job id - {id}")


def main():
    s = sched.scheduler(time.monotonic, time.sleep)
    for i in range(10):
        s.enter(i, 1, job, argument=(i,))
    
    print("Starting job ...")
    s.run()


if __name__ == "__main__":
    main()

