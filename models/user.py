from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from dataclasses_json import dataclass_json
from models.playlist import PlayList, Playlist


@dataclass_json
@dataclass
class User:
    playlists: List[Playlist] = field(default_factory=list)

    id: int = 0
    uuid: str = ""
    user_name: str = ""
    hashed_password: str = ""
    passsword_salt: str = ""
    modified: datetime = datetime.utcnow()
    created: datetime = datetime.utcnow()
    is_deleted: bool = False