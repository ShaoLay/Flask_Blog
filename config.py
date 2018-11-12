from app import app


# class Config(object):
#激活跨站点请求伪造保护
CSRF_ENABLED = True
# 项目秘钥
app.SECRET_KEY = 'q7pBNcWPgmF6BqB6b5VICF7z7pI'

# 配置Mysql数据库连接信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:970202@127.0.0.1:3306/Flask_Blog'
# 是否追踪数据库的修改：不追踪(节省开销)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True