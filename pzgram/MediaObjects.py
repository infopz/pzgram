from .Api import *


class GenericMedia:
    def __init__(self, bot, dict):
        self.bot = bot
        for i in dict:
            setattr(self, i, dict[i])

    def save(self, path):
        if hasattr(self, "file_path"):
            # Some Media already have the file_path attrivure
            download_file(self.bot, self.file_path, path)
        else:
            # Media dont have file_path, so i retrive it with getFile method
            file = api_request(self.bot, "getFile", {"file_id": self.file_id})
            download_file(self.bot, file["file_path"], path)


class Photo(GenericMedia):
    pass


class Voice(GenericMedia):
    pass
