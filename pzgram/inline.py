import json
from typing import TYPE_CHECKING

from .api import api_request
from .objects import Message, User

if TYPE_CHECKING:
    from .bot import Bot


class CallbackQuery:

    attributes = ["id", "sender", "message", "inline_message_id", "chat_instance", "data", "game_short_name"]

    def __init__(self, bot: "Bot", callback_dict: dict):
        self.bot = bot
        for i in self.attributes:
            if i in callback_dict:
                setattr(self, i, callback_dict[i])
            else:
                setattr(self, i, None)
        # Parse Sender
        s = callback_dict.pop("from")
        self.sender = User(bot, s["id"], s)
        # Parse Message if exists
        try:
            m = callback_dict.pop("message")
            self.message = Message(self.bot, m["message_id"], m)
        except KeyError:
            self.message = None

    def reply(self, text: str=None, allert: bool=None, url: str=None, cache_time: int=None) -> dict:
        p = {
            "callback_query_id": self.id,
            "text": text,
            "show_allert": allert,
            "url": url,
            "cache_time": cache_time
        }
        return api_request(self.bot, "answerCallbackQuery", p)


def create_button(text: str, data: str=None, url: str=None) -> dict:
    if (data is not None and url is not None) or (data is None and url is None):
        raise Exception("You must pass exactly 2 parameter to create_button")
    if data is not None:
        return {"text": text, "callback_data": data}
    else:
        # if url is not none
        return {"text": text, "url": url}


def create_inline(array: list) -> str:
    inline = {"inline_keyboard": array}
    return json.dumps(inline)
