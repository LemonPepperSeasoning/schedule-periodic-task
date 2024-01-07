import threading, time
from task import task, TASK_FREQUENCY


class RepeatedTimer(object):
  def __init__(self, interval, function, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False


if __name__ == "__main__":
    print("starting...")
    rt = RepeatedTimer(TASK_FREQUENCY, task, "my-param") # it auto-starts, no need of rt.start()
    try:
        time.sleep(10) # your long-running job goes here...
    finally:
        rt.stop() # better in a try/finally block to make sure the program ends!
