from dotenv import dotenv_values

key = dotenv_values(".env")
class Config:
    SECRET_KEY = key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskdb.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
