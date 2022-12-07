import logging

from todoist_api_python.models import Task
from todoist_service.todoist_wrapper.todoist_wrapper import TodoistWrapper


class RemoveTime:
    def __init__(self, doist: TodoistWrapper):
        self.doist = doist

    def remove_time(self, task:Task):
        title = task.content
        task_date = task.due
        if task_date is None:
            logging.info("skipping %s. doesn't have due date" % task_date)
            return

        task_time = task_date.datetime
        if not has_time(task_time=task_time):
            logging.info("skipping %s. didn't have a time" % task_time)
            return

        new_task_time = task_time.split("T")[0]
        logging.info(
            "set {title} to {task_time}".format(title=title, task_time=new_task_time)
        )
        self.doist.update_task(task.id,due={"datetime": new_task_time})
        self.doist.commit()


def has_time(task_time: str):
    return ":" in task_time
