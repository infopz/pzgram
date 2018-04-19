import threading
import traceback

from .objects import *
from .useful import notafunction as nf
from .useful import *
from .exceptions import *
from .inline import CallbackQuery


class Bot:
    def __init__(self, bot_key: str):
        self.key = bot_key
        self.offset = 0
        # Bot Informations
        self.id = None
        self.username = None
        self.name = None
        # Bot Functions
        self.processAll = nf
        self.processMessage = nf
        self.startFunc = nf
        self.endFunc = nf
        self.editFunc = nf
        self.channelPostFunc = nf
        self.editChannelPostFunc = nf
        self.callBackFunc = nf
        # Bot Settings
        self.APITimeout = 100
        # Others
        self.timers = dict()
        self.commands = {"start": default_start, "help": default_help}
        self.query = dict()
        self.next_func = dict()
        self.next_query = dict()
        print(time_for_log() + "Bot Created")

    def run(self) -> None:
        # Check bot key and receive bot information
        try:
            bot_data = api_request(self, 'getMe')
        except ApiError:
            # If raise ApiError means that the token is not valid
            print(time_for_log() + "ApiKey Error: Token is not valid")
            print(time_for_log() + "Shutdown...")
            return
        self.id = bot_data["id"]
        self.username = bot_data["username"]
        self.name = bot_data["first_name"]
        # Call start function before starting the bot
        call(self.startFunc, {"bot": self})
        if len(self.timers):
            # For each timer create a different thread
            for t in self.timers:
                threading.Thread(target=self.run_timer, args=(self.timers[t], t), daemon=True).start()
        print(time_for_log() + self.name + " Started")
        try:
            self.run_bot()
        except KeyboardInterrupt:
            print(time_for_log() + "Shutdown...")
            call(self.endFunc, {"bot": self})

    def run_bot(self) -> None:
        while True:
            updates = self.get_updates()
            for i in updates:
                # Create a thread for each update
                threading.Thread(target=self.run_update, args=(i,), daemon=True).start()

    def get_updates(self) -> dict:
        while True:
            param = {
                "offset": self.offset,
                "timeout": self.APITimeout
            }
            # Create a local timeout, just in case of breaking connection
            local_timeout = self.APITimeout + 2
            try:
                updates = api_request(self, "getUpdates", param, timeout=local_timeout)
            except TelegramConnectionError:
                # If connection error, retry in 5 seconds
                print(time_for_log() + "ConnectionError: can't reach Telegram servers. Retry in 5s")
                time.sleep(5)
                continue
            except ApiError:
                # Api Error if another client is getting update
                print(time_for_log() + "ApiError - Another program is getting updates for this bot. Retry in 5s")
                time.sleep(5)
                continue
            # If the returned array contains at least 1 update
            if len(updates):
                # Increase the offset
                self.offset = updates[-1]["update_id"] + 1
                return updates

    def run_update(self, update: dict) -> None:
        # If the update contains a Message
        if "message" in update:
            message = Message(self, update["message"]["message_id"], update["message"])
            chat = message.chat
            possible_args = {"message": message, "chat": chat, "sender": message.sender,
                             "args": message.args, "bot": self}
            # Call processAll function passing all the possible args
            # If Function return something, stop running this update
            if call(self.processAll, possible_args):
                return
            if message.type == "command":
                if chat.id in self.next_func:
                    # Remove the set_next if arrives a new command
                    self.next_func.pop(chat.id, None)
                if message.command in self.commands:
                    call(self.commands[message.command], possible_args)
                else:
                    # If command is not in list, send message with /help
                    call(command_not_found, possible_args)
            elif chat.id in self.next_func:
                # Call next func if it setted for that chat.id
                func = self.next_func.pop(chat.id)
                call(func, possible_args)
            else:  # For every message that is not a command or in next_func
                call(self.processMessage, possible_args)
        elif "edited_message" in update:
            if self.editFunc != nf:
                message = Message(self, update["edited_message"]["message_id"], update["edited_message"])
                possible_args = {"message": message, "chat": message.chat, "sender": message.sender,
                                 "args": message.args, "bot": self}
                # Call the related function
                call(self.editFunc, possible_args)
        elif "channel_post" in update:
            if self.channelPostFunc != nf:
                message = Message(self, update["channel_post"]["message_id"], update["channel_post"])
                possible_args = {"message": message, "chat": message.chat,
                                 "args": message.args, "bot": self}
                # Call the related function
                call(self.channelPostFunc, possible_args)
        elif "edited_channel_post" in update:
            if self.editChannelPostFunc != nf:
                message = Message(self, update["edited_channel_post"]["message_id"], update["edited_channel_post"])
                possible_args = {"message": message, "chat": message.chat,
                                 "args": message.args, "bot": self}
                # Call the related function
                call(self.editChannelPostFunc, possible_args)
        elif "callback_query" in update:
            # Parse CallbackQuery
            query = CallbackQuery(self, update["callback_query"])
            possible_args = {"query": query, "message": query.message, "sender": query.sender,
                             "data": query.data, "chat": query.message.chat}
            # If is in the query dict
            if query.data is not None and query.data in self.query:
                call(self.query[query.data], possible_args)
            # Otherwise
            elif self.callBackFunc != nf:
                call(self.callBackFunc, possible_args)

    def set_commands(self, command_dict: dict) -> None:
        # Used to avoid overwring of default start and help if not included
        for i in command_dict:
            self.commands[i] = command_dict[i]

    def set_query(self, query_dict: dict) -> None:
        for i in query_dict:
            self.query[i] = query_dict[i]

    def run_timer(self, timer_function: "function", delay: int) -> None:
        while True:
            try:
                timer_function()
            except:
                print("")
                traceback.print_exc()
            time.sleep(calc_new_delay(delay))

    def set_next(self, chat: Chat, func: "function") -> None:
        self.next_func[chat.id] = func
