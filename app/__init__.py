import os

from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import Config, basedir

app = Flask(__name__)

app.config.from_object(Config)
# 创建SQLALCHEMY对象
db = SQLAlchemy(app)
redis_store = None

Session(app)

login = LoginManager(app)
login.login_view = 'login'
openid = OpenID(app, os.path.join(basedir, 'tmp'))


# 注册路由
from .index import index_blue
app.register_blueprint(index_blue)


