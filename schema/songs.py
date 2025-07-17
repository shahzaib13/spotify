from sqlalchemy import Column, Integer, Text, VARCHAR, DateTime, func
from base import Base

class SongTable(Base):
    __tablename__ = "songs"
    id = Column(Text, primary_key=True, index=True)
    name = Column(VARCHAR(200), nullable=False)
    artist = Column(VARCHAR(200), nullable=False)
    category = Column(VARCHAR(200), nullable=True)
    thumbnail = Column(Text)
    url = Column(Text, nullable=False)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
