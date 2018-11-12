from flask_session import Session
from redis import StrictRedis

class Config(object):
    """工程配置信息"""
    DEBUG = True

    # 数据库的配置信息
    # 配置Mysql数据库连接信息
    SQLALCHEMY_DATABASE_URI = 'mysql://root:970202@127.0.0.1:3306/Flask_Blog'
    # 是否追踪数据库的修改：不追踪(节省开销)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 指定session使用什么来存储
    SESSION_TYPE = 'redis'
    # 指定session数据存储在后端的位置
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 是否使用secret_key签名你的sessin
    SESSION_USE_SIGNER = True
    # 设置过期时间，要求'SESSION_PERMANENT', True。而默认就是31天
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 24  # 一天有效期

    # 开启csrf保护
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'






