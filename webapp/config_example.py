import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_ID = "yourclient_id_here.apps.googleusercontent.com"
    CLIENT_SECRET = "your_client_secret"
    REDIRECT_URI = 'https://localhost:5000/gCallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']
