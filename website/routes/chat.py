import json
import datetime as dt

from flask import (Flask, render_template, url_for, redirect, Blueprint)
from flask_login import current_user, login_required

from core import config
from database import DatabaseManager
from functions import *

chat = Blueprint('chat', __name__, static_folder='../static/', template_folder='../templates/chat')
logger = Logger(config)
database_manager = DatabaseManager(config.DATABASE)

@chat.route('/', methods=['GET'])
@login_required
def index():
    return redirect(url_for('chat.home'))

@chat.route('/home')
@login_required
def home():
    with database_manager as session:
        rooms = session.query(database_manager.ChatRoom).all()
    return render_template('chat.html', rooms=rooms)

@chat.route('/room/<string:room_id>')
@login_required
def room(room_id):
    with database_manager as session:
        current_room = session.query(database_manager.ChatRoom).filter_by(id=room_id).first()
        all_rooms = session.query(database_manager.ChatRoom).all()
        messages = sorted(session.query(database_manager.ChatMessage).filter_by(room_id=room_id).all(), key=lambda message: message.datetime)

        for message in messages:
            message.sender = session.query(database_manager.User).filter_by(id=message.sender_id).first()
            message.date_filtered = message.datetime.strftime('%b %d %Y %I:%M %p')
        
        for message in messages:
            message.meta_data = json.loads(message.meta_data)
        
    return render_template('chat.html', room=current_room, rooms=all_rooms, messages=messages, current_user_meta=json.loads(current_user.meta_data))

@chat.route('/room-detailed/<string:room_id>')
@login_required
def room_detailed(room_id):

    with database_manager as session:
        room = session.query(database_manager.ChatRoom).filter_by(id=room_id).first()
        room.creation_date_filtered  = room.creation_date.strftime('%B %d %Y %H:%M.%S %p')
        room.room_creator = session.query(database_manager.User).filter_by(id=room.room_creator_id).first()

    return render_template('room-detailed.html', room=room)