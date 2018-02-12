from .Useful import message_types as types
from .Useful import message_all_attributes as message_all
from .Api import api_request


class Message:
    def __init__(self, botkey, message_dict):
        self.botkey = botkey
        # Find the type of this message
        for t in types:
            if t in message_dict:
                self.type = t
                break
        # Add all possbile attributes to message_dict and set to None
        for i in message_all:
            if i not in message_dict:
                message_dict[i] = None
        # Delete attribute from and replace with sender
        message_dict["sender"] = User(botkey, message_dict["from"])
        message_dict.pop("from")
        message_dict["chat"] = Chat(botkey, message_dict["chat"]["id"], message_dict["chat"])
        # Memorize all attributes
        for i in message_dict:
            setattr(self, i, message_dict[i])

    def reply(self, text, **kwargs):
        return self.chat.send(text, reply_to=self.message_id, **kwargs)


class Chat:
    def __init__(self, botkey, id, chat_dict=dict()):
        self.botkey = botkey
        self.id = id
        for i in chat_dict:
            setattr(self, i, chat_dict[i])

    def send(self, text, parse_mode="markdown", preview=True, notification=True, reply_to=None, reply_markup=None):
        param = {
            "chat_id": self.id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": not preview,
            "disable_notification": notification,
            "reply_to_message_id": reply_to,
            "reply_markup": reply_markup
        }
        return Message(self.botkey, api_request(self.botkey, "sendMessage", param))


class User:
    def __init__(self, botkey, user_dict):
        self.botkey = botkey
        for i in user_dict:
            setattr(self, i, user_dict[i])

    def send(self, text, **kwargs):
        Chat(self.botkey, self.id).send(text, **kwargs)
