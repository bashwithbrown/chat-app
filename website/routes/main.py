from flask import (Flask, url_for, redirect, Blueprint)
from core import config

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return redirect(url_for('auth.login'))