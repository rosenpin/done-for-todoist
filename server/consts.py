import pathlib

SERVER_PORT = 9991

# Page locations
SETTINGS_PAGE_LOCATION = "settings"

# HTML related consts
HTML_CHECKED = "checked"
HTML_CURRENT_USER_PH = "{{USER_ID}}"
HTML_CURRENT_MODE_PH = '{{CURRENT_MODE}}'

# Paths
SETTINGS_PAGE = pathlib.Path(__file__).parent.parent / "resources/settings.html"
HOME_PAGE = pathlib.Path(__file__).parent.parent / "resources/index.html"
FAVICON = pathlib.Path(__file__).parent.parent / "resources/favicon.png"

# URLS
SERVER_REDIRECT_URL = "https://done.rosenpin.io/redirect"
TODOIST_AUTHORIZE_URL = "https://todoist.com/oauth/authorize"
TODOIST_TOKEN_URL = 'https://todoist.com/oauth/access_token'

# Todoist related consts
TODOIST_PREMISSIONS = "data:read_write"

# Param names
PARAM_STATE = "state"
PARAM_ACCESS_TOKEN = "access_token"
PARAM_CODE = "code"
WEB_HOOK_USER_ID_FIELD = "user_id"

# Cookie names
COOKIE_STATE = "state"
COOKIE_USERID = "user_id"

# Workaround proxy
INNER_SERVER = "http://0.0.0.0:9991"
OUTER_SERVER = "https://done.rosenpin.io"

# Webhook related consts
WEB_HOOK_TASK_ID = "id"
WEB_HOOK_TASK_DATA = "event_data"
WEB_HOOK_CHECKED = "checked"

# Error Messages
WEBHOOK_ERROR_MESSAGE = "Error in webhook for request:\n\n {request}:\n\n {error}"
SERVER_ERROR_MESSAGE = "Server error: \n\n{error}"
USER_NOT_FOUND_MESSAGE = "user with user_id %s not found in db"

# HTTP codes
HTTP_USER_ERROR = 401
HTTP_SERVER_ERROR = 501

db_path = pathlib.Path.home().joinpath("done-for-todoist-users.json")
