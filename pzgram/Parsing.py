from .Useful import notafunction as nf
from .MediaObjects import *


def parse_text(message_dict, bot):
    if message_dict["text"].startswith("/"):
        message_dict["command"] = message_dict["text"].split()[0][1:]
        message_dict["args"] = message_dict["text"].split()[1:]
        return message_dict, "command"
    return message_dict


def parse_audio(message_dict, bot):
    message_dict["audio"] = Audio(bot, message_dict["audio"])
    return message_dict


def parse_photo(message_dict, bot):
    photo_array = []
    for p in message_dict["photo"]:
        photo_array.append(Photo(bot, p))
    message_dict["photo"] = photo_array
    return message_dict


def parse_voice(message_dict, bot):
    message_dict["voice"] = Voice(bot, message_dict["voice"])
    return message_dict


def parse_document(message_dict, bot):
    message_dict["document"] = Document(bot, message_dict["document"])
    return message_dict


message_types = {
    "text": parse_text,
    "audio": parse_audio,
    "document": parse_document,
    "game": nf,
    "photo": parse_photo,
    "sticker": nf,
    "video": nf,
    "voice": parse_voice,
    "video_note": nf,
    "caption": nf,
    "contact": nf,
    "location": nf,
    "venue": nf,
    "new_chat_members": nf,
    "left_chat_member": nf,
    "new_chat_title": nf,
    "new_chat_photo": nf,
    "delete_chat_photo": nf,
    "group_chat_created": nf,
    "supergroup_chat_created": nf,
    "channel_chat_created": nf,
    "migrate_to_chat_id": nf,
    "migrate_from_chat_id": nf,
    "pinned_message": nf
}