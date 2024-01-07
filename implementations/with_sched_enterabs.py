import sched, time


def job(id=0):
    print(f"{time.monotonic()} - running job id - {id}")


def main():
    s = sched.scheduler(time.monotonic, time.sleep)
        

    current_time = round(time.monotonic())
    for i in range(10):
        print(current_time+i)
        s.enterabs(current_time+i, 1,  job, argument=(i,))


    print("starting job ...")
    s.run()



if __name__ == "__main__":
    main()
