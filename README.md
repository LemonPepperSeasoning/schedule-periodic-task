# Schedule Periodic Task

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository explores various implementations of a task scheduler in Python, with a focus on scheduling periodic tasks. The primary objective is to investigate methods for minimizing or eliminating drift during the scheduled tasks.

## Best Implementation

For heavy-heavy task that requires distributed computation, I would recommend using Celery. ([Celery-implemetation](implementations/with_celery.py)) Its easy to setup & there is no drift as well.

For lighter I/O bound task, using Manual scheduling plus the use of Threading should be sufficient. ([Manual-scheduling-with-Threading](implementations/with_manual_scheduling_using_thread.py))

For ligher CPU bound task, use Multiprocessing instead. ([Manual-scheduling-with-process](implementations/with_manual_scheduling_using_process.py))

Honourable mentions.
The `Sched` library from the Python Standard Library allows you to schedule multiple tasks in advance, offering a more efficient approach compared to scheduling tasks individually on the main thread in other implementations. (see [Sched-implementation](implementations/with_sched_v2.py))

## Experiments and Results

### Experiment Overview

The repository conducts extensive experiments to assess the reliability of each implementation method. Key metrics include:

- **Drift Measurement:** Analyze the total drift observed over extended periods (e.g., 1 hour, 1 day).
- **Asynchronicity:** Explore the feasibility of implementing tasks asynchronously.

### Results

#### Drift Measurement

TBD, but in summary, avoid using the schedule library if drift is a concern. Ensure tasks run in a different thread or process to prevent blocking the main thread and hindering the scheduling of subsequent tasks

### Acknowledgments

- [StackOverflow ideas](https://stackoverflow.com/questions/474528/how-to-repeatedly-execute-a-function-every-x-seconds/25251804#25251804)

- [Medium Article on related topic](https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679)
