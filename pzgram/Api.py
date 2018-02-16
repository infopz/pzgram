import requests

from .Exceptions import *


def api_request(bot, method, param=None, files=None, timeout=None):
    try:
        data = requests.post("https://api.telegram.org/bot" + bot.key + "/" + method,
                             data=param, files=files, timeout=timeout)
    except KeyboardInterrupt:
        raise
    except:
        raise TelegramConnectionError("Error with the request for the method " + method)
    data = data.json()
    if not data['ok']:
        raise ApiError("Error returned from telegram: " + str(data["error_code"]) + " - " + data["description"])
    return data['result']


def download_file(bot, telegram_path, save_path):
    url = "https://api.telegram.org/file/bot" + bot.key + "/" + telegram_path
    r = requests.get(url, allow_redirects=True)
    open(save_path, "wb").write(r.content)
