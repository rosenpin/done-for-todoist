import logging

from todoist_api_python.models import Task
from todoist_service.todoist_wrapper.todoist_wrapper import TodoistWrapper

from logic.strikethrough import Strikethrough
from logic.remove_time import RemoveTime


class Logic:
    def __init__(self, doist: TodoistWrapper):
        self.doist = doist
        self.striker = Strikethrough(doist=doist)
        self.time_remover = RemoveTime(doist=doist)

    def __handle_task(self, task: Task, checked: int):
        if checked == 1:
            self.striker.strike(task=task)
            self.time_remover.remove_time(task=task)
        if checked == 0:
            self.striker.unstrike(task=task)

    def run_specific_task(self, task_id, checked):
        logging.info("running for specific task {task_id}".format(task_id=task_id))

        task = self.doist.get_task_by_id(task_id)

        self.__handle_task(task=task, checked=checked)
