from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer, Float, MetaData, DateTime, Text)

from flask_login import UserMixin

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    username = Column(String(100), unique=True)
    password = Column(String(100))
    meta_data = Column(Text)

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(String, primary_key=True, unique=True)
    datetime = Column(DateTime)
    name = Column(String)
    email = Column(String)
    meta_data = Column(Text)

class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(String, primary_key=True, unique=True)
    dates = Column(Text)
    status = Column(String)
    title = Column(String)
    meta_data = Column(Text)

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(String, primary_key=True, unique=True)
    due_date = Column(DateTime)
    task = Column(String)
    status = Column(String)

class ContactMessage(Base):
    __tablename__ = 'contact_messages'
    id = Column(String, primary_key=True, unique=True)
    datetime = Column(DateTime)
    contact_id = Column(String)
    message = Column(String)

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