from celery import Celery
from celery.schedules import crontab
from task import task, TASK_FREQUENCY


app = Celery()
app.conf.broker_url = 'redis://localhost:6379/0'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    print("Setting up ...")
    sender.add_periodic_task(
        1.0, 
        my_celery_task.s('my-param'), 
        name='my-task',
        expires=10
    )

    print("Finished setup")


@app.task
def my_celery_task(args):
    task(args)


if __name__ == "__main__":
    print("Starting app ...")

