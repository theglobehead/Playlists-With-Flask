from datetime import datetime
from typing import List
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from models.artist import Artist

from models.tag import Tag


@dataclass_json
@dataclass
class Song:
    tags: List[Tag] = field(default_factory=list)
    artist = Artist

    id: int = 0
    name: str = ""
    album: str = ""
    audio_path: str = ""
    modified: datetime = datetime.utcnow()
    created: datetime = datetime.utcnow()
    is_deleted: bool = False