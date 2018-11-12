from flask_sqlalchemy import SQLAlchemy




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





