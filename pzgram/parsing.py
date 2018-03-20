import collections

from .useful import notafunction as nf
from .media_objects import *


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


def parse_video(message_dict, bot):
    message_dict["video"] = Video(bot, message_dict["video"])
    return message_dict


def parse_contact(message_dict, bot):
    message_dict["contact"] = Contact(bot, message_dict["contact"])
    return message_dict


def parse_videonote(message_dict, bot):
    message_dict["video_note"] = VideoNote(bot, message_dict["video_note"])
    return message_dict


def parse_location(message_dict, bot):
    message_dict["location"] = Location(bot, message_dict["location"])
    return message_dict


def parse_venue(message_dict, bot):
    message_dict["venue"] = Venue(bot, message_dict["venue"])
    message_dict["location"] = message_dict["venue"].location
    return message_dict

# Used a orderdDict to parse correctly the Venue
message_types = collections.OrderedDict()
message_types["text"] = parse_text
message_types["audio"] = parse_audio
message_types["document"] = parse_document
message_types["game"] = nf
message_types["photo"] = parse_photo
message_types["sticker"] = nf
message_types["video"] = parse_video
message_types["voice"] = parse_voice
message_types["video_note"] = parse_videonote
message_types["caption"] = nf
message_types["contact"] = parse_contact
message_types["venue"] = parse_venue
message_types["location"] = parse_location
message_types["new_chat_members"] = nf
message_types["left_chat_member"] = nf
message_types["new_chat_title"] = nf
message_types["new_chat_photo"] = nf
message_types["delete_chat_photo"] = nf
message_types["group_chat_created"] = nf
message_types["supergroup_chat_created"] = nf
message_types["channel_chat_created"] = nf
message_types["migrate_to_chat_id"] = nf
message_types["migrate_from_chat_id"] = nf
message_types["pinned_message"] = nf
