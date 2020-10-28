import getpass
import os

from flask import Flask, redirect, request, make_response, send_file
from oauthlib.oauth2 import WebApplicationClient
from todoist_service.db import DB
from todoist_service.server.authorization.authorization import AuthorizationHandler

import utils
from consts import credentials
from . import consts
from .consts import *
from .handlers import handle_web_hook, handle_settings, handle_logout

DEBUG = getpass.getuser() == "tomer"
if DEBUG:
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)

client = WebApplicationClient(credentials.CLIENT_ID)
authorization_handler = AuthorizationHandler(SERVER_REDIRECT_URL,
                                             INNER_SERVER,
                                             OUTER_SERVER,
                                             credentials.CLIENT_ID,
                                             credentials.CLIENT_SECRET,
                                             TODOIST_PREMISSIONS)


@app.route("/")
def index():
    try:
        user_id = request.cookies.get(COOKIE_USERID)
        if user_id:
            return redirect(SETTINGS_PAGE_LOCATION)

        with open(HOME_PAGE, 'r') as file:
            data = file.read()
            return make_response(data)
    except Exception as err:
        utils.log_error(err)
        return make_response(SERVER_ERROR_MESSAGE.format(error=err))


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        handle_web_hook(db=DB.get_instance(consts.db_path))
    except Exception as err:
        utils.log_error(err)

    return make_response("", 200)


@app.route("/settings")
def settings():
    try:
        response = handle_settings(db=DB.get_instance(consts.db_path))
        return response
    except Exception as err:
        utils.log_error(err)
        return make_response(SERVER_ERROR_MESSAGE.format(error=err), HTTP_SERVER_ERROR)


@app.route("/logout")
def logout():
    try:
        response = handle_logout(db=DB.get_instance(consts.db_path))
        return response
    except Exception as err:
        utils.log_error(err)
        return make_response(SERVER_ERROR_MESSAGE.format(error=err), HTTP_SERVER_ERROR)


@app.route('/authorize')
def authorize():
    try:
        response = authorization_handler.handle_authorization_request(client=client)
        return response
    except Exception as err:
        utils.log_error(err)
        return SERVER_ERROR_MESSAGE.format(error=err)


@app.route("/redirect")
def redirect_url():
    try:
        response = authorization_handler.handle_redirect_request(client=client, db=DB.get_instance(consts.db_path))
        return response
    except Exception as err:
        utils.log_error(err)
        return SERVER_ERROR_MESSAGE.format(error=err)


@app.route("/favicon.png")
def favicon():
    return send_file(FAVICON)


@app.route("/calendar-option.png")
def calendar_option():
    return send_file(CALENDAR_OPTION_IMG)


def run_server():
    app.run(port=SERVER_PORT, debug=DEBUG)
