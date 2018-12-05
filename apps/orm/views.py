from flask import Blueprint, render_template
from sqlalchemy import and_, or_

from .models import Category

orm = Blueprint('orm', __name__)


@orm.route('/')
def find():
    # 关系运算符    !=  > <  <= >=  ==
    Category.query.filter(Category.name != '')
    #  in  like  between  and    and or
    # SELECT  * FROM WHERE  cate_id in (1,2,3)
    query = Category.query.filter(Category.cate_id.in_([1, 2, 3]))
    cate_list = query.all()

    # SELECT  * FROM  CATE  WHERE name like  '%欧%'

    # cate_list = Category.query.filter(Category.name.like('%美'), Category.cate_id == 1).all()

    # cate_list = Category.query.filter(and_(Category.cate_id == 1, Category.name.like('%美'))).all()

    # query = Category.query.filter(Category.cate_id.in_([1, 2, 3]))
    # cate_list = Category.query.filter(or_(Category.cate_id == 1, Category.name == '非洲')).all()
    cate_list = Category.query.filter(Category.cate_id.between(1, 100))
    # 过滤列
    # entity
    cate_list = Category.query.with_entities(Category.cate_id, Category.name).all()
    data = []
    for cate in cate_list:
        data.append({'cate_id': cate[0], 'name': cate[1]})

        # select * from  表名
        #     select 列名 别名, .... from 表名
        #     select 列名 别名, .... FROM   表名    WHERE 条件
        #     SELECT  列名  别名 ,....FROM  表名
        #     where  条件
        #     group by 字段,   having  分组过滤的条件
        #     order by 字段[ASC | DESC]....
        #     多表
        #     外连接   全外连接(mysql不支持)   左外连接  右外连接
        #     表名  别名  LEFT  OUTER JOIN 表名 别名
        #     表名 别名   right outer  join
        #     using(外键关联字段)  on  关联字段=关联字段
    return render_template('cates.html', cate_list=data)


@orm.route('/list/<int:page>/<int:size>/')
def pagination_view(page, size):
    pagination = Category.query.paginate(page=page, per_page=size, error_out=False)
    # 获取多少页
    print(pagination.pages)
    # 当前的数据
    print(pagination.items)
    # 总条数
    print(pagination.total)
    # 当前的页码
    print(pagination.page)
    # 是否有上一页
    print(pagination.has_prev)
    # 是否有下一页
    print(pagination.has_next)
    # 当前页显示多少条数据
    print(pagination.prev_num)
    # 下一页页显示多少条数据
    print(pagination.next_num)
    """
    left_edge=2 左边最少显示两条数据
    left_current=2 当前页左边显示最少2条数据
    right_current=5 //当前页右边显示5条数据,包含本省
    right_edge=5    // 右边最少显示5条记录
    """
    # pagination.iter_pages(left_edge=2, left_current=2,
    #                       right_current=5, right_edge=2)
    left_current = 5
    right_current = 5
    if page < 6:
        right_current = 11 - page
    elif pagination.pages - page < 5:
        left_current = 9 - (pagination.pages - page)

    return render_template('pagination.html', pagination=pagination, left_current=left_current,
                           right_current=right_current)


@orm.route('/cate/')
def cate():
    cates = Category.query.all()
    return render_template('cates.html', cates=cates)
