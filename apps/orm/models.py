import datetime

from apps.ext import db


class Category(db.Model):
    # 主键
    cate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), unique=True, index=True, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    status = db.Column(db.Boolean, default=True)
