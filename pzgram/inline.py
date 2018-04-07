import json

from .api import api_request
from .objects import Message, User


class CallbackQuery:

    attributes = ["id", "sender", "message", "inline_message_id", "chat_instance", "data", "game_short_name"]

    def __init__(self, bot, callback_dict):
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

    def reply(self, text=None, allert=None, url=None, cache_time=None):
        p = {
            "callback_query_id": self.id,
            "text": text,
            "show_allert": allert,
            "url": url,
            "cache_time": cache_time
        }
        return api_request(self.bot, "answerCallbackQuery", p)


def create_button(text, data=None, url=None):
    if data is not None and url is not None:
        print("Error")
        # FIXME
    if data is not None:
        return {"text": text, "callback_data": data}
    else:
        return {"text": text, "url": url}


def create_inline(array):
    inline = {"inline_keyboard": array}
    return json.dumps(inline)
