import collections

from .media_objects import *


def parse_forward_reply(message_dict, bot):
    if "forward_from" in message_dict:
        from .objects import User
        message_dict["forward_from"] = User(bot, message_dict["forward_from"])
    if "forward_from_chat" in message_dict:
        from .objects import Chat
        message_dict["forward_from_chat"] = Chat(bot, message_dict["forward_from"])
    if "reply_to_message" in message_dict:
        from .objects import Message
        message_dict["reply_to_message"] = Message(bot, message_dict["reply_to_message"])
    return message_dict


def df(message_dict, bot):
    # Default Parsing Func, used when no actions are required, or that type is not supported yet
    return message_dict


def parse_text(message_dict, bot):
    if message_dict["text"].startswith("/"):
        split = message_dict["text"].split()
        # Insert another split with @ to avoid error with /try@mybot
        message_dict["command"] = split[0][1:].split("@")[0]
        message_dict["args"] = split[1:]
        # Add the "type" key to dict, in order to change the type from text to command
        message_dict["type"] = "command"
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


def parse_new_user(message_dict, bot):
    from .objects import User
    new_users = []
    # Convert all dict in User object
    for u in message_dict["new_chat_members"]:
        new_users.append(User(bot, u))
    message_dict["new_chat_members"] = new_users
    # Delete useless keys
    message_dict.pop("new_chat_participant", None)
    message_dict.pop("new_chat_member", None)
    return message_dict


def parse_left_user(message_dict, bot):
    from .objects import User
    message_dict["left_chat_member"] = User(bot, message_dict["left_chat_member"])
    message_dict.pop("left_chat_participant", None)


def parse_new_chat_photo(message_dict, bot):
    photos = []
    for p in message_dict["new_chat_photo"]:
        photos.append(Photo(bot, p))
    message_dict["new_chat_photo"] = photos
    return message_dict


def parse_pinned_message(message_dict, bot):
    from .objects import Message
    message_dict["pinned_message"] = Message(bot, message_dict["pinned_message"])
    return message_dict


# Used a orderdDict to parse correctly the Venue
message_types = collections.OrderedDict()
message_types["text"] = parse_text
message_types["audio"] = parse_audio
message_types["document"] = parse_document
message_types["game"] = df
message_types["photo"] = parse_photo
message_types["sticker"] = df
message_types["video"] = parse_video
message_types["voice"] = parse_voice
message_types["video_note"] = parse_videonote
message_types["contact"] = parse_contact
message_types["venue"] = parse_venue
message_types["location"] = parse_location
message_types["new_chat_members"] = parse_new_user
message_types["left_chat_member"] = parse_left_user
message_types["new_chat_title"] = df
message_types["new_chat_photo"] = parse_new_chat_photo
message_types["delete_chat_photo"] = df
message_types["group_chat_created"] = df
message_types["supergroup_chat_created"] = df
message_types["channel_chat_created"] = df
message_types["migrate_to_chat_id"] = df
message_types["migrate_from_chat_id"] = df
message_types["pinned_message"] = parse_pinned_message
