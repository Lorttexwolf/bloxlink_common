# These are intended structures/models that are to be used across Bloxlink products, and other modules.

from dataclasses import dataclass, field
from contextlib import suppress
from typing import Any
from enum import Enum
import datetime
import copy


__all__ = [
    "UserData", 
    "GuildData",
    "MinimalRobloxUser",
    "ExtendedRobloxUser",
    "RobloxThumbnailSizes"
]

def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))

class PartialMixin:
    __slots__ = ()

    def __getattr__(self, name: str) -> Any:
        with suppress(AttributeError):
            return super().__getattr__(name)

    def __getattribute__(self, __name: str) -> Any:
        with suppress(AttributeError):
            return super().__getattribute__(__name)

@dataclass(slots=True)
class UserData(PartialMixin):
    '''User data stored in the Bloxlink Database.'''
    id: int
    robloxID: str = None
    robloxAccounts: dict = default_field({"accounts":[], "guilds": {}})

@dataclass(slots=True)
class GuildData:
    id: int
    binds: list = default_field([]) # FIXME

    verifiedRoleEnabled: bool = True
    verifiedRoleName: str = "Verified" # deprecated
    verifiedRole: str = None

    unverifiedRoleEnabled: bool = True
    unverifiedRoleName: str = "Unverified" # deprecated
    unverifiedRole: str = None

class RobloxThumbnailSizes(Enum):
    AVATAR_48x48 = "48x48"
    AVATAR_60x60 = "60x60"
    AVATAR_75x75 = "75x75"
    AVATAR_100x100 = "100x100"
    AVATAR_110x110 = "110x110"
    AVATAR_160x160 = "160x160"
    AVATAR_250x250 = "250x250"
    AVATAR_352x352 = "352x352"
    AVATAR_420x420 = "420x420"
    
    
@dataclass(slots=True)
class MinimalRobloxUser():
    '''Represents the minimal structure of a Roblox user.'''
    id: int = -1 # -1 represents un-set id.

@dataclass(slots=True)
# Retrieve from the enhanced Roblox user retrieval API https://bloxlink-info-server-vunlj.ondigitalocean.ap
class ExtendedRobloxUser(MinimalRobloxUser):
    username: str = None
    banned: bool = None
    age_days: int = None
    groups: dict = None
    avatar: str = None
    description: str = None
    display_name: str = None
    created: datetime.datetime = None
    badges: list = None
    short_age_string: str = None
    flags: int = None
    overlay: int = None
    
    