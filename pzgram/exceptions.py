
class ApiError(Exception):
    pass


class TelegramConnectionError(Exception):
    pass


class FileNotFoundError(Exception):
    pass


class WrongChatTypeError(Exception):
    pass
