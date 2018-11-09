import os


class Config(object):
    #激活跨站点请求伪造保护
    CSRF_ENABLED = True
    SECTET_KEY = 'you-will-never-guess' #

    basedir = os.path.abspath(os.path.dirname(__file__))

    # 数据库文件路径
    SQLALCHEMY_DATABASE_URI = 'sqllite:///' + os.path.join(basedir, 'app.db')
    # 数据库文件存储
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
