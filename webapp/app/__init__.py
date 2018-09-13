from flask import Flask
from app.config import Config

app = Flask(__name__)
config = Config()

from app import routes
