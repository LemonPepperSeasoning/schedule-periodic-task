import sched, time
from task import task


def print_some_times():
    print(time.time())
    s.enter(10, 1, task)
    s.enter(5, 2, task, argument=('positional',))
    # despite having higher priority, 'keyword' runs after 'positional' as enter() is relative
    s.enter(5, 1, task, kwargs={'id': 1})
    #s.enterabs(1_650_000_000, 10, task, argument=("first enterabs",))
    #s.enterabs(1_650_000_000, 5, task, argument=("second enterabs",))
    s.run()
    print(time.time())


if __name__ == "__main__":
    s = sched.scheduler(time.monotonic, time.sleep)
    print_some_times()

