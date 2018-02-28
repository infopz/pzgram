import os

from .Parsing import message_types
from .Useful import message_all_attributes as message_all
from .Useful import file_name
from .Api import *

from .MediaObjects import *


class Message:
    def __init__(self, bot, message_dict):
        self.bot = bot
        # Find the type of this message
        for t in message_types:
            if t in message_dict:
                self.type = t
                # Call the connected method for parsing that type of message
                res = message_types[t](message_dict, bot)
                # Check if return 1 or 2 values (First is the dict, Second is the new type)
                if isinstance(res, tuple):
                    message_dict = res[0]
                    self.type = res[1]
                else:
                    message_dict = res
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
        # Memorize all attributes
        for i in message_dict:
            setattr(self, i, message_dict[i])

    def reply(self, text, **kwargs):
        return self.chat.send(text, reply_to=self.message_id, **kwargs)

    def reply_photo(self, photopath, **kwargs):
        return self.chat.send_photo(photopath, reply_id=self.message_id, **kwargs)

    def reply_voice(self, voicepath, **kwargs):
        return self.chat.send_voice(voicepath, reply_id=self.message_id, **kwargs)

    def reply_audio(self, audiopath, **kwargs):
        return self.chat.send_voice(audiopath, reply_id=self.message_id, **kwargs)

    def reply_document(self, documentpath, **kwargs):
        return self.chat.send_voice(documentpath, reply_id=self.message_id, **kwargs)

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

    def send_document(self, documentpath, caption=None, parse_mode=None,
                      notification=True, reply_id=None, reply_markup=None):
        # Check if file exists
        if not os.path.isfile(documentpath):
            raise FileNotFoundError("File " + documentpath + " not exists or is a folder")
        # Find the name of that file from his path
        name = file_name(documentpath)
        file = {
            "document": (name, open(documentpath, "rb"))
        }
        param = {
            "chat_id": self.id,
            "caption": caption,
            "parse_mode": parse_mode,
            "disable_notification": not notification,
            "reply_to_message_id": reply_id,
            "reply_markup": reply_markup
        }
        return Message(self.bot, api_request(self.bot, "sendDocument", param, file))


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

    def send_audio(self, audiopath, **kwargs):
        return Chat(self.bot, self.id).send_voice(audiopath, **kwargs)

    def send_document(self, documentpath, **kwargs):
        return Chat(self.bot, self.id).send_voice(documentpath, **kwargs)