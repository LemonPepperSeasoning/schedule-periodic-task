#### Running Celery implementation

Requirements:

- redis
- celery (`pip install celery[redis]`)

> **_NOTE:_** I used redis but other brokers (sqs, rabbitmq, etc) can also be used.

To run, Open 3 terminal

```
# on first terminal run;
redis-server

# on second terminal run;
celery -A with_celery worker    # to run the worker. ie, node that execute the task

# on third terminal run;
celery -A with_celery beat -l debug      # to run the task-scheduler
```
