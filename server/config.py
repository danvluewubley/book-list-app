from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager 
from dotenv import dotenv_values

key = dotenv_values(".env")

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flaskdb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = key

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)