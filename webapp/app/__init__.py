from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from config import Config
from redis import Redis
import rq
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.session_protection = 'strong'
socketio = SocketIO(app)
bootstrap = Bootstrap(app)

app.redis = Redis.from_url(app.config['REDIS_URL'])
app.task_queue = rq.Queue('tasks', connection=app.redis)

app.app_context().push()

from app import routes, models
