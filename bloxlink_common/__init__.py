# These are intended structures/models that are to be used across Bloxlink products, and other modules.

from dataclasses import dataclass, field
from contextlib import suppress
from typing import Any, Callable, Iterable
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

# TODO: Implement types for binds.
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
    
    def get_binds(self, bind_type: str):
        '''Retrieves all binds that match the given bind type.'''
        return [bind for bind in self.binds if bind["bind"]["type"] == bind_type]
    
    def find_bind(self, bind_type: str, predicate: Callable):
        '''Retrieves the first bind that matches the given type and predicate.'''
        for bind in self.get_binds(bind_type):
            if predicate(bind):
                return bind
        return None
    

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
class ExtendedRobloxUserGroupEntryData:
    id: int = -1
    name: str = None
    memberCount: int = -1
    hasVerifiedBadge: bool = False

@dataclass(slots=True)
class ExtendedRobloxUserGroupEntryRole:
    id: int = -1
    name: str = None
    rank: int = -1

# Might be an easier way to represent an object, with these keys using the typing lib.
@dataclass(slots=True)
class ExtendedRobloxUserGroupEntry:
    group: ExtendedRobloxUserGroupEntryData
    role: ExtendedRobloxUserGroupEntryRole

@dataclass(slots=True)
# Retrieve from the enhanced Roblox user retrieval API https://bloxlink-info-server-vunlj.ondigitalocean.ap
class ExtendedRobloxUser(MinimalRobloxUser):
    username: str = None
    banned: bool = None
    age_days: int = None
    groups: list[ExtendedRobloxUserGroupEntry] = field(default_factory=lambda: [])
    avatar: str = None
    description: str = None
    display_name: str = None
    created: datetime.datetime = datetime.datetime.now()
    badges: list = None
    short_age_string: str = None
    flags: int = None
    overlay: int = None