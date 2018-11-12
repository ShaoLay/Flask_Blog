from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)

app.config.from_object(Config)
# 创建SQLALCHEMY对象
db = SQLAlchemy(app)
redis_store = None

Session(app)


# 注册路由
from app.index import index_blue
app.register_blueprint(index_blue)


