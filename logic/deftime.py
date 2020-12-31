import logging

from todoist_service.consts import TaskFields
from todoist_service.todoist_wrapper.todoist_wrapper import TodoistWrapper

STRIKE = "\u0336"

class TimeSetter:
    def __init__(self, doist: TodoistWrapper):
        self.doist = doist

    def set_time(self, task):
        title = task[TaskFields.Title]
        if already_annotated(title=title):
            logging.info("skipping %s. already annotated" % title)
            return

        new_title = strike_text(title)
        logging.info("set {title} to {new_title}".format(title=title, new_title=new_title))
        task.update(content=new_title)
        self.doist.commit()
