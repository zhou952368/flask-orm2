from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# 初始化第三方插件
def init_ext(app):
    init_db(app)


db = SQLAlchemy()
migrate = Migrate()


# 初始化数据库
def init_db(app):
    # 数据的连接的路径
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask_orm2?charset=utf8'
    # 打印sql语句
    app.config['SQLALCHEMY_ECHO'] = True
    # 自动提交事务
    # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app=app, db=db)
