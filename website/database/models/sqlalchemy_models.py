from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, MetaData, DateTime, Text)

from flask_login import UserMixin

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    username = Column(String(100), unique=True)
    password = Column(String(100))
    meta_data = Column(Text)

class ChatMessage(Base):
    __tablename__ = 'chat_messages'
    id = Column(String, primary_key=True, unique=True)
    datetime = Column(DateTime, nullable=False)
    message = Column(String, nullable=False)
    sender_id = Column(String, nullable=False)
    room_id = Column(String, nullable=False)
    meta_data = Column(Text, nullable=False)

class ChatRoom(Base):
    __tablename__ = 'chat_rooms'
 
    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=True)
    creation_date = Column(DateTime, nullable=False)
    room_creator_id = Column(String(255), nullable=False)