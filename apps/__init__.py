from flask import Flask

# 程序的入口
from apps.ext import init_ext
from apps.orm.views import orm
from apps.req.views import req
from apps.temp.controller import temp
from apps.temp.filters import test_filter


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456'
    app.debug = True
    register(app)
    register_filter(app)
    init_ext(app)
    return app


def register(app: Flask):
    app.register_blueprint(orm)
    app.register_blueprint(temp)
    app.register_blueprint(req)


def register_filter(app: Flask):
    app.add_template_filter(test_filter, 'test')
