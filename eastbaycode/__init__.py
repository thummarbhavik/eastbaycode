from flask import Flask
from eastbaycode.config import Config

app = Flask(__name__)
config = Config()

from eastbaycode import routes
