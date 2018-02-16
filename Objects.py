from .Useful import message_types as types
from .Useful import message_all_attributes as message_all
from .Api import api_request


class Message:
    def __init__(self, bot, message_dict):
        self.bot = bot
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
        message_dict["sender"] = User(bot, message_dict["from"])
        message_dict.pop("from")
        message_dict["chat"] = Chat(bot, message_dict["chat"]["id"], message_dict["chat"])
        # Check if text is command and create args
        if message_dict["text"].startswith("/"):
            message_dict["command"] = message_dict["text"].split()[0][1:]
            message_dict["args"] = message_dict["text"].split()[1:]
            self.type = "command"
        # Memorize all attributes
        for i in message_dict:
            setattr(self, i, message_dict[i])

    def reply(self, text, **kwargs):
        return self.chat.send(text, reply_to=self.message_id, **kwargs)


class Chat:
    def __init__(self, bot, id, chat_dict=dict()):
        self.bot = bot
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
        return Message(self.bot, api_request(self.bot, "sendMessage", param))

    def send_action(self, action):
        param = {"chat_id": self.id, "action": action}
        print(api_request(self.bot, "sendChatAction", param))


class User:
    def __init__(self, bot, user_dict):
        self.botkey = bot
        for i in user_dict:
            setattr(self, i, user_dict[i])

    def send(self, text, **kwargs):
        return Chat(self.bot, self.id).send(text, **kwargs)
