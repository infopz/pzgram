import inspect
import time
import json

message_all_attributes = [
    "message_id", "from", "date", "chat",
    "forward_from", "forward_from_chat", "forward_from_message_id", "forward_from_signature",
    "reply_to_message", "edit_date", "media_group_id", "author_signature",
    "text", "entities", "caption_entities", "audio", "document", "game", "photo", "sticker", "video",
    "voice", "video_note", "caption", "contact", "location", "venue",
    "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
    "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
    "migrate_to_chat_id", "pinned_message"
]  # TODO: paymets

message_types = [
    "text", "audio", "document", "game", "photo", "sticker", "video",
    "voice", "video_note", "caption", "contact", "location", "venue",
    "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
    "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
    "migrate_to_chat_id", "pinned_message"
]

chat_all_attributes = [
    "id", "type", "title", "username", "first_name", "last_name", "all_members_are_administrator",
    "photo", "description", "invite_link", "pinned_message", "sticker_set_name", "can_set_sticker_set"
]

user_all_attirbutes = [
    "id", "is_bot", "first_name", "last_name", "username", "language_code"
]


def notafunction():
    """Default functions for some parts of bot"""
    pass


def call(f, args):
    """Function that call a function passing him the requested args"""
    # Get Function Args
    f_args = inspect.getfullargspec(f).args
    to_pass = []
    # Add to to_pass all the args requested
    for i in f_args:
        to_pass.append(args[i])
    return f(*to_pass)


def default_start(chat, message, bot):
    """Default function for /start command"""
    chat.send("Hi *" + message.sender.first_name + "*, Welcome on @" + bot.username + "\nUse /help to view all commands")


def default_help(chat, bot):
    """Default funcion for /help command"""
    text = ""
    for i in bot.commands:
        if i != "help" and i != "start":
            docstring = bot.commands[i].__doc__
            if docstring is None:
                text += "  /" + i + "\n"
            else:
                text += "  /" + i + " - " + docstring + "\n"
    if text == "":
        chat.send("There is no command connected to this bot")
    else:
        chat.send("These are the possible commands\n" + text)


def command_not_found(chat, message):
    """Send an error message if user ask a command that not exists"""
    chat.send("/" + message.command + " not found\nUse /help to view all possible commands")


def time_for_log():
    """Function that print the current time for bot prints"""
    return time.strftime("%d/%m %H:%M:%S - ")


def calc_new_delay(delay):
    """Calc the dalay of timer based on what time is it"""
    seconds_today = (time.localtime().tm_hour * 3600) + (time.localtime().tm_min * 60) + time.localtime().tm_sec
    passed_from_last = seconds_today % delay
    new_delay = delay - passed_from_last
    return new_delay


def create_keyboard(keyboard_array, resize=True, one_time=False):
    keyboard = {"keyboard": keyboard_array, "resize_keyboard": resize, "one_time_keyboard": one_time}
    keyboard = json.dumps(keyboard)
    return keyboard
