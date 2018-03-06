from .Api import *

# TODO: send
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
    """Extension .jpg .png"""
    pass


class Voice(GenericMedia):
    """Extension .ogg"""
    pass


class Audio(GenericMedia):
    """Extension .mpeg .mp3"""
    pass


class Video(GenericMedia):
    """Extension .mp4"""
    def __init__(self, bot, dict):
        GenericMedia.__init__(self, bot, dict)
        # Parse thumb as Photo object if exists
        if hasattr(self, "thumb"):
            self.thumb = Photo(bot, self.thumb)


class Document(GenericMedia):
    def __init__(self, bot, dict):
        GenericMedia.__init__(self, bot, dict)
        # Parse thumb as Photo object if exists
        if hasattr(self, "thumb"):
            self.thumb = Photo(bot, self.thumb)

# TODO: send
class Contact:
    def __init__(self, bot, contact_dict):
        self.bot = bot
        for i in contact_dict:
            setattr(self, i, contact_dict[i])