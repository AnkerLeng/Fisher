from flask import jsonify, request

from app.forms.book import SearchForm
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


# 蓝图blueprint 蓝本

# @web.route('/book/search/<q>/<page>')
@web.route('/book/search')
def search():
    """
    q:普通关键字 isbn
    page
    """
    # q = request.args['q']
    # page = request.args['page']
    # print(q, page)
    # a = request.args.to_dict()

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
        # return json.dumps(result), 200, {'content-type': 'application/json'}

    else:
        return jsonify(form.errors)
