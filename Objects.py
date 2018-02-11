

class Message:
    def __init__(self, message_dict, edited=False):
        for i in message_dict:
            setattr(self, i, message_dict[i])
        self.chat = Chat(self.chat)
        self.type = "text"  # TODO: Include other types
        # TODO Create command attribute if type=command

class Chat:
    # TODO: Methods send
    def __init__(self, chat_dict):
        for i in chat_dict:
            setattr(self, i, chat_dict[i])


class User:
    # TODO: Methods send
    def __init__(self, user_dict):
        for i in user_dict:
            setattr(self, i, user_dict[i])
