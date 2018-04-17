import requests
from typing import Union, TYPE_CHECKING

from .exceptions import *

if TYPE_CHECKING:
    from .bot import Bot


def api_request(bot: "Bot", method: str, param: dict=None, files: dict=None, timeout: int=None):
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


def download_file(bot: "Bot", telegram_path: str, save_path: str) -> None:
    url = "https://api.telegram.org/file/bot" + bot.key + "/" + telegram_path
    r = requests.get(url, allow_redirects=True)
    open(save_path, "wb").write(r.content)
