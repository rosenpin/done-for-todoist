import logging

from todoist_service.consts import TaskFields
from todoist_service.todoist_wrapper.todoist_wrapper import TodoistWrapper

STRIKE = "\u0336"
DURATION_FORMAT = "{original} [{duration}m]"


def unstrike_text(before: str):
    return before.replace(STRIKE, "")


def strike_text(before: str):
    after = ""
    for i in before:
        after = after + STRIKE + i
    after = after + STRIKE
    return after


def already_annotated(title) -> bool:
    return STRIKE in title


class Strikethrough:
    def __init__(self, doist: TodoistWrapper):
        self.doist = doist

    def strike(self, task):
        title = task[TaskFields.Title]
        if already_annotated(title=title):
            logging.info("skipping %s. already annotated" % title)
            return

        new_title = strike_text(title)
        logging.info("set {title} to {new_title}".format(title=title, new_title=new_title))
        task.update(content=new_title)
        self.doist.commit()

    def unstrike(self, task):
        title = task[TaskFields.Title]
        if not already_annotated(title=title):
            logging.info("skipping %s. not yet annotated" % title)
            return

        new_title = unstrike_text(title)
        logging.info("set {title} to {new_title}".format(title=title, new_title=new_title))
        task.update(content=new_title)
        self.doist.commit()
