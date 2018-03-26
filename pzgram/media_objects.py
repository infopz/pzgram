from .api import *


class GenericMedia:
    def __init__(self, bot, dict):
        self.bot = bot
        for i in dict:
            setattr(self, i, dict[i])

    def __str__(self):
        return "MediaObject" + self.file_id

    def save(self, path):
        if hasattr(self, "file_path"):
            # Some Media already have the file_path attribure
            download_file(self.bot, self.file_path, path)
        else:
            # Media dont have file_path, so i retrive it with getFile method
            file = api_request(self.bot, "getFile", {"file_id": self.file_id})
            download_file(self.bot, file["file_path"], path)


class Photo(GenericMedia):
    """Extension .jpg .png"""


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


class VideoNote(GenericMedia):
    """Rounded Square .mp4 Video"""
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


class Contact:
    def __init__(self, bot, contact_dict):
        self.bot = bot
        for i in contact_dict:
            setattr(self, i, contact_dict[i])


class Location:
    def __init__(self, bot, location_dict):
        self.bot = bot
        for i in location_dict:
            setattr(self, i, location_dict[i])


class Venue:
    def __init__(self, bot, venue_dict):
        self.bot = bot
        for i in venue_dict:
            setattr(self, i, venue_dict[i])
        self.location = Location(bot, venue_dict["location"])
