import os

from .Useful import message_types as types
from .Useful import message_all_attributes as message_all
from .Useful import file_name
from .Api import *

from .MediaObjects import *


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
        # FIXME: Check if this work with Channels or Groups
        message_dict["sender"] = User(bot, message_dict["from"])
        message_dict.pop("from")
        message_dict["chat"] = Chat(bot, message_dict["chat"]["id"], message_dict["chat"])
        # Parse Photo if exists
        if self.type == "photo":
            photo_array = []
            for p in message_dict["photo"]:
                photo_array.append(Photo(bot, p))
            message_dict["photo"] = photo_array
        # Parse Voice
        elif self.type == "voice":
            message_dict["voice"] = Voice(self.bot, message_dict["voice"])
        # Parse Audio
        elif self.type == "audio":
            message_dict["audio"] = Audio(self.bot, message_dict["audio"])
        # Check if text is command and create args
        elif self.type == "text" and message_dict["text"].startswith("/"):
            message_dict["command"] = message_dict["text"].split()[0][1:]
            message_dict["args"] = message_dict["text"].split()[1:]
            self.type = "command"
        # Memorize all attributes
        for i in message_dict:
            setattr(self, i, message_dict[i])

    def reply(self, text, **kwargs):
        return self.chat.send(text, reply_to=self.message_id, **kwargs)

    def reply_photo(self, photopath, **kwargs):
        return self.chat.send_photo(photopath, reply_id=self.message_id, **kwargs)

    def reply_voice(self, voicepath, **kwargs):
        return self.chat.send_voice(voicepath, reply_id=self.message_id, **kwargs)


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
        return api_request(self.bot, "sendChatAction", param)

    def send_photo(self, photopath, caption=None, parse_mode=None, notification=True, reply_id=None, reply_markup=None):
        # Check if file exists
        if not os.path.isfile(photopath):
            raise FileNotFoundError("File " + photopath + " not exists or is a folder")
        # Find the name of that file from his path
        name = file_name(photopath)
        file = {
            "photo": (name, open(photopath, "rb"))
        }
        param = {
            "chat_id": self.id,
            "caption": caption,
            "parse_mode": parse_mode,
            "disable_notification": not notification,
            "reply_to_message_id": reply_id,
            "reply_markup": reply_markup
        }
        return Message(self.bot, api_request(self.bot, "sendPhoto", param, file))

    def send_voice(self, voicepath, duration=None, caption=None, parse_mode=None,
                   notification=True, reply_id=None, reply_markup=None):
        # Check if file exists
        if not os.path.isfile(voicepath):
            raise FileNotFoundError("File " + voicepath + " not exists or is a folder")
        # Find the name of that file from his path
        name = file_name(voicepath)
        file = {
            "voice": (name, open(voicepath, "rb"))
        }
        param = {
            "chat_id": self.id,
            "duration": duration,
            "caption": caption,
            "parse_mode": parse_mode,
            "disable_notification": not notification,
            "reply_to_message_id": reply_id,
            "reply_markup": reply_markup
        }
        return Message(self.bot, api_request(self.bot, "sendVoice", param, file))

    def send_audio(self, audiopath, duration=None, performer=None, title=None, caption=None, parse_mode=None,
                   notification=True, reply_id=None, reply_markup=None):
        # Check if file exists
        if not os.path.isfile(audiopath):
            raise FileNotFoundError("File " + audiopath + " not exists or is a folder")
        # Find the name of that file from his path
        name = file_name(audiopath)
        file = {
            "audio": (name, open(audiopath, "rb"))
        }
        param = {
            "chat_id": self.id,
            "duration": duration,
            "performer": performer,
            "title": title,
            "caption": caption,
            "parse_mode": parse_mode,
            "disable_notification": not notification,
            "reply_to_message_id": reply_id,
            "reply_markup": reply_markup
        }
        return Message(self.bot, api_request(self.bot, "sendAudio", param, file))


class User:
    def __init__(self, bot, user_dict):
        self.bot = bot
        for i in user_dict:
            setattr(self, i, user_dict[i])

    def send(self, text, **kwargs):
        return Chat(self.bot, self.id).send(text, **kwargs)

    def send_photo(self, photopath, **kwargs):
        return Chat(self.bot, self.id).send_photo(photopath, **kwargs)

    def send_voice(self, voicepath, **kwargs):
        return Chat(self.bot, self.id).send_voice(voicepath, **kwargs)