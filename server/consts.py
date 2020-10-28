import pathlib

SERVER_PORT = 9991

SETTINGS_PAGE_LOCATION = "settings"

# HTML related consts
HTML_CURRENT_USER_PH = "{{USER_ID}}"

# Paths
SETTINGS_PAGE = pathlib.Path(__file__).parent.parent / "resources/settings.html"
HOME_PAGE = pathlib.Path(__file__).parent.parent / "resources/index.html"
FAVICON = pathlib.Path(__file__).parent.parent / "resources/favicon.png"
CALENDAR_OPTION_IMG = pathlib.Path(__file__).parent.parent / "resources/calendar-option.png"

# URLS
SERVER_REDIRECT_URL = "https://done.rosenpin.io/redirect"

# Todoist related consts
TODOIST_PREMISSIONS = "data:read_write"

# Param names
WEB_HOOK_USER_ID_FIELD = "user_id"

# Cookie names
COOKIE_USERID = "user_id"

# Workaround proxy
INNER_SERVER = "http://0.0.0.0:9991"
OUTER_SERVER = "https://done.rosenpin.io"

# Webhook related consts
WEB_HOOK_TASK_ID = "id"
WEB_HOOK_TASK_DATA = "event_data"
WEB_HOOK_CHECKED = "checked"

# Error Messages
SERVER_ERROR_MESSAGE = "Server error: \n\n{error}"

# HTTP codes
HTTP_SERVER_ERROR = 501

db_path = pathlib.Path.home().joinpath("done-for-todoist-users.json")
