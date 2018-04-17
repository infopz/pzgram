import inspect
import time
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .bot import Bot
    from .objects import Chat, Message

# https://youtu.be/hrsvRDeIfbo
# Però tinàm bòta cun forza cunvinta
# Modena l’è fort la’ns da brisa per vinta!


def notafunction(*args, **kwargs):
    """Default functions for some parts of bot"""
    pass


def call(f: 'function', args: dict):
    """Function that call a function passing him the requested args"""
    # Get Function Args
    f_args = inspect.getfullargspec(f).args
    to_pass = []
    # Add to to_pass all the args requested
    for i in f_args:
        to_pass.append(args[i])
    return f(*to_pass)


def default_start(chat: "Chat", message: "Message", bot: "Bot") -> None:
    """Default function for /start command"""
    chat.send("Hi *" + message.sender.first_name + "*, Welcome on @" + bot.username +
              "\nUse /help to view all commands")


def default_help(chat: "Chat", bot: "Bot") -> None:
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


def command_not_found(chat: "Chat", message: "Message") -> None:
    """Send an error message if user ask a command that not exists"""
    chat.send("/" + message.command + " not found\nUse /help to view all possible commands")


def time_for_log() -> str:
    """Function that print the current time for bot prints"""
    return time.strftime("%d/%m %H:%M:%S - ")


def calc_new_delay(delay: int) -> int:
    """Calc the dalay of timer based on what time is it"""
    seconds_today = (time.localtime().tm_hour * 3600) + (time.localtime().tm_min * 60) + time.localtime().tm_sec
    passed_from_last = seconds_today % delay
    new_delay = delay - passed_from_last
    return new_delay


def create_keyboard(keyboard_array: list, resize: bool=True, one_time: bool=False) -> str:
    keyboard = {"keyboard": keyboard_array, "resize_keyboard": resize, "one_time_keyboard": one_time}
    keyboard = json.dumps(keyboard)
    return keyboard


def remove_keyboard() -> str:
    return json.dumps({"remove_keyboard": True})


def force_reply() -> str:
    return json.dumps({"force_reply": True})


def file_name(path: str) -> str:
    """From path of a file, find the name of that file"""
    # Scroll back path string until he find / or \
    for i in range(len(path)-1, 0, -1):
        if path[i] == "/" or path[i] == "\\":
            return path[i+1:]
    else:
        return path
