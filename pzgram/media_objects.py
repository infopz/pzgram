from .api import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .bot import Bot


class GenericMedia:
    def __init__(self, bot: "Bot", dict: dict):
        self.bot = bot
        for i in self.attributes:
            if i in dict:
                setattr(self, i, dict[i])
            else:
                setattr(self, i, None)
        # Some media already have file_path
        if "file_path" in dict:
            self.file_path = dict["file_path"]

    def __str__(self) -> str:
        return "MediaObject" + str(self.file_id)

    def save(self, path: str) -> None:
        if hasattr(self, "file_path"):
            # Some Media already have the file_path attribure
            download_file(self.bot, self.file_path, path)
        else:
            # Media dont have file_path, so i retrive it with getFile method
            file = api_request(self.bot, "getFile", {"file_id": self.file_id})
            download_file(self.bot, file["file_path"], path)


class Photo(GenericMedia):
    """Extension .jpg .png"""
    attributes = ["file_id", "width", "height", "file_size"]


class Voice(GenericMedia):
    """Extension .ogg"""
    attributes = ["file_id", "duration", "mime_type", "file_size"]


class Audio(GenericMedia):
    """Extension .mpeg .mp3"""
    attributes = ["file_id", "duration", "performer", "title", "mime_type", "file_size"]


class Video(GenericMedia):
    """Extension .mp4"""

    attributes = ["file_id", "width", "height", "duration", "thumb", "mime_type", "file_size"]

    def __init__(self, bot: "Bot", dict: dict):
        GenericMedia.__init__(self, bot, dict)
        # Parse thumb as Photo object if exists
        if self.thumb is not None:
            self.thumb = Photo(bot, self.thumb)


class VideoNote(GenericMedia):
    """Rounded Square .mp4 Video"""

    attributes = ["file_id", "lenght", "duration", "mime_type", "file_size"]

    def __init__(self, bot: "Bot", dict: dict):
        GenericMedia.__init__(self, bot, dict)
        # Parse thumb as Photo object if exists
        if self.thumb is not None:
            self.thumb = Photo(bot, self.thumb)


class Sticker(GenericMedia):
    """Exstension .webp"""

    attributes = ["file_id", "width", "height", "thumb", "emoji", "set_name", "mask_position", "file_size"]

    def __init__(self, bot: "Bot", dict: dict):
        GenericMedia.__init__(self, bot, dict)
        # Parse thumb as Photo object if exists
        if self.thumb is not None:
            self.thumb = Photo(bot, self.thumb)


class Document(GenericMedia):
    """Generic Document"""

    attributes = ["file_id", "thumb", "file_name", "mime_type", "file_size"]

    def __init__(self, bot: "Bot", dict: dict):
        GenericMedia.__init__(self, bot, dict)
        # Parse thumb as Photo object if exists
        if self.thumb is not None:
            self.thumb = Photo(bot, self.thumb)


class Contact:

    attributes = ["phone_number", "first_name", "last_name", "user_id"]

    def __init__(self, bot: "Bot", contact_dict: dict):
        self.bot = bot
        for i in self.attributes:
            if i in contact_dict:
                setattr(self, i, contact_dict[i])
            else:
                setattr(self, i, None)

    def __str__(self) -> str:
        return "ContactObject" + str(self.first_name)


class Location:

    def __init__(self, bot: "Bot", location_dict: dict):
        self.bot = bot
        self.longitude = location_dict["longitude"]
        self.latitude = location_dict["latitude"]

    def __str__(self) -> str:
        return "LocationObject{" + str(self.latitude) + "|" + str(self.longitude) + "}"


class Venue:

    attibutes = ["location", "title", "address", "foursquare_id"]

    def __init__(self, bot: "Bot", venue_dict: dict):
        self.bot = bot
        for i in self.attributes:
            if i in venue_dict:
                setattr(self, i, venue_dict[i])
            else:
                setattr(self, i, None)
        self.location = Location(bot, venue_dict["location"])

    def __str__(self) -> None:
        return "VenueObject" + self.title
