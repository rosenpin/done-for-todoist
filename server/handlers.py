import threading

from flask import request, redirect, make_response
from todoist_service.db import DB
from todoist_service.todoist_wrapper.todoist_api_wrapper import TodoistAPIWrapper

import utils
from logic import logic
from .consts import *


def handle_user_task(db: DB, user_id, task_id, checked: int):
    doist = TodoistAPIWrapper(token=db.get_user_by_user_id(user_id=user_id).token)
    logic.Logic(doist=doist).run_specific_task(task_id=task_id, checked=checked)


def handle_web_hook(db):
    req = request.json

    user_id = req[WEB_HOOK_USER_ID_FIELD]
    task_id = req[WEB_HOOK_TASK_DATA][WEB_HOOK_TASK_ID]
    checked = req[WEB_HOOK_TASK_DATA][WEB_HOOK_CHECKED]

    try:
        db.get_user_by_user_id(user_id=user_id)
    except KeyError:
        utils.log_error("User not found, skipping")
        return

    threading.Thread(target=handle_user_task, kwargs={
        'db': db,
        'user_id': user_id,
        'task_id': task_id,
        'checked': checked
    }).start()


def handle_settings(db):
    user_id = request.cookies.get(COOKIE_USERID)
    if not user_id:
        return redirect("/")

    try:
        user = db.get_user_by_user_id(user_id=user_id)
    except KeyError as err:
        utils.log_error(err)
        response = redirect("/")
        response.delete_cookie(COOKIE_USERID)
        return response

    with open(SETTINGS_PAGE, 'r') as file:
        data = file.read()

        data = add_user_name(data, user)

        return make_response(data)


def add_user_name(page, user):
    return page.replace(HTML_CURRENT_USER_PH, user.user_name)


def handle_logout(db: DB):
    user_id = request.cookies.get(COOKIE_USERID)
    if not user_id:
        return redirect("/")

    db.remove_user_by_user_id(user_id=user_id)
    response = redirect("/")
    response.delete_cookie(COOKIE_USERID)
    return response
