# from flask import Flask
# from secrets import token_hex


# UPLOAD_FOLDER = 'app/static/uploads'
# SECRET_KEY = token_hex(16)


# app = Flask(__name__)

# app.config['SEND_FILE_MAXIMUM_AGE_DEFAULT'] = 0
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['SECRET_KEY'] = SECRET_KEY


# from app import main
# # We import the main module at the bottom and not at the top to prevent Flask from throwing errors
# # resulting from circular imports. This is because the main module will also need the app variable to be imported.



# __init__.py

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from config import SECRET_KEY
import os

UPLOAD_FOLDER = 'app/static/uploads'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artistry.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import main
