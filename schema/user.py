from sqlalchemy import Column, Text, VARCHAR, LargeBinary
from base import Base

class UserTable(Base):
    __tablename__ = "users"  

    id = Column(Text, primary_key=True, index=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100), unique=True, nullable=False)
    profile_pic = Column(Text, nullable=True)
    password = Column(LargeBinary, nullable=False)
