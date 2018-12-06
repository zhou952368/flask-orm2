import datetime

from flask import Blueprint, render_template

from apps.orm.models import Category

temp = Blueprint('temp', __name__, template_folder='templates')


# 自定义过滤器


@temp.route('/demo/')
def temp1():
    return render_template('demo.html')


# /temps?page=1$size=10

@temp.route('/temps/<int:page>/<int:size>/')
def temps(page, size):
    pagination = Category.query.paginate(page=page, per_page=size, error_out=False)
    return render_template('temps.html', pagination=pagination, items=pagination.items)
