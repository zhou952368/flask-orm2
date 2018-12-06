from flask import Blueprint, request, render_template, flash, redirect, url_for

req = Blueprint('req', __name__, template_folder='templates')


@req.route('/hello/', methods=['get', 'post', 'put', 'delete', 'head'])
def hello():
    print(request.headers)
    if request.method == 'GET':
        request.args.get('name')
        # 相当于post请求
        # request.form
        # 获取文件的对象
        # request.files
        # 获取cookie信息
        # request.cookies
        # 获取的是解析好的json字符串
        # request.json
        # 获取原生的数据   当是json数据的时候,获取的 json字符串
        # request.get_data()
        # values既能获取get请求的数据也能获取post的数据
        # request.values
        print(request.values.get('name'))
    elif request.method == 'POST':
        print(request.values.get('name'))
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    return ''


@req.route('/flash/')
def flash_view():
    flash('分类闪现', 'error')
    flash('对不起,你知道的太多了')
    return render_template('flash.html')


@req.route('/redirect/')
def redirect_view():
    return redirect(url_for('.flash_view'))
