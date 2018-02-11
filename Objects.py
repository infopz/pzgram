from .Useful import message_types as types
from .Useful import message_all_attributes as message_all


class Message:
    def __init__(self, message_dict):
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
        message_dict["sender"] = User(message_dict['from'])
        message_dict.pop("from")
        message_dict["chat"] = Chat(message_dict["chat"])
        # Memorize all attributes
        for i in message_dict:
            setattr(self, i, message_dict[i])


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
