from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SongsModel(BaseModel):
    name: str
    artist: str
    url: str
    thumbnail: str
    category: str
    likes : Optional[int] = 0
    created_at: Optional[datetime] = None
