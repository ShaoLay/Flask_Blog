import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_openid import OpenID
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import Config, basedir
# from app.index import views,  errors
# from app import models

app = Flask(__name__)

app.config.from_object(Config)
# 创建SQLALCHEMY对象
db = SQLAlchemy(app)
redis_store = None

Session(app)

login = LoginManager(app)
login.login_view = 'login'
openid = OpenID(app, os.path.join(basedir, 'tmp'))
mail = Mail(app)


# 注册路由
from .index import index_blue
app.register_blueprint(index_blue)

# 程序出现bug，给管理员发送邮件 & 记录到日志中去
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')