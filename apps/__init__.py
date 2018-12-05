from flask import Flask

# 程序的入口
from apps.ext import init_ext
from apps.orm.views import orm


def create_app():
    app = Flask(__name__)
    app.debug = True
    register(app)
    init_ext(app)
    return app


def register(app: Flask):
    app.register_blueprint(orm)
