import threading

from .Api import api_request
from .Objects import *
from .Useful import notafunction as nf
from .Useful import *


class Bot:
    def __init__(self, bot_key):
        self.key = bot_key
        self.offset = 0
        # Bot Informations
        self.id = None
        self.username = None
        self.name = None
        # Bot Functions
        self.processAll = nf
        self.processMessage = nf
        # Bot Settings
        self.acceptEdited = False
        self.acceptOlder = False
        # Others
        self.timers = dict()
        self.commands = {"start": default_start, "help": default_help}

    def run(self):
        # Check bot key and receive bot information
        bot_data = api_request(self.key, 'getMe')
        self.id = bot_data["id"]
        self.username = bot_data["username"]
        self.name = bot_data["first_name"]
        if len(self.timers):
            # TODO: Start timers
            pass
        self.run_bot()

    def run_bot(self):
        while True:
            updates = self.get_updates()
            for i in updates:
                # Create a thread for each update
                threading.Thread(target=self.run_update, args=(i,), daemon=True).start()

    def get_updates(self):
        while True:
            param = {
                "offset": self.offset,
                "timeout": 10
            }
            updates = api_request(self.key, "getUpdates", param)
            # If the returned array contains at least 1 update
            if len(updates):
                # Increase the offset
                self.offset = updates[-1]["update_id"] + 1
                return updates

    def run_update(self, update):
        # If the update contains a Message
        if "message" in update:
            message = Message(self.key, update["message"])
            chat = message.chat
            possibile_args = {"message": message, "chat": chat, "bot": self}
            # Call processAll function passing all the possible args
            # If Function return something, stop running this update
            if call(self.processAll, possibile_args):
                return
            if message.type == "command":
                call(self.commands[message.command], possibile_args)
            else:  # For every message that is not a command
                call(self.processMessage, possibile_args)

    def set_commands(self, command_dict):
        # Used to avoid overwring of default start and help if not included
        for i in command_dict:
            self.commands[i] = command_dict[i]
