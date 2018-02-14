import requests

from .Exceptions import *


def api_request(botkey, method, param=None, timeout=None):
    try:
        data = requests.post("https://api.telegram.org/bot" + botkey + "/" + method, data=param, timeout=timeout)
    except KeyboardInterrupt:
        raise
    except:
        raise RequestsError("Error with the request for the method " + method)
    data = data.json()
    if not data['ok']:
        raise ApiError("Error returned from telegram: " + str(data["error_code"]) + " - " + data["description"])
    return data['result']
    # TODO Manage Same Key