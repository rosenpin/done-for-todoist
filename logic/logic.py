import logging

from todoist.models import Item
from todoist_service.todoist_wrapper.todoist_wrapper import TodoistWrapper

from logic.deftime import TimeSetter


class Logic:
    def __init__(self, doist: TodoistWrapper):
        self.doist = doist
        self.striker = TimeSetter(doist=doist)

    def __handle_task(self, task: Item, checked: int):
        if checked == 1:
            self.striker.strike(task=task)
        if checked == 0:
            self.striker.unstrike(task=task)

    def run_specific_task(self, task_id, checked):
        logging.info("running for specific task {task_id}".format(task_id=task_id))

        task = self.doist.get_task_by_id(task_id)

        self.__handle_task(task=task, checked=checked)
