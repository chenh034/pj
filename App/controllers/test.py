import glo
from flask import jsonify
from App import app
from gevent import monkey

from App.models.article import Article

monkey.patch_all()

DB = glo.get_value('DB')


@app.route('/test/<int:user>')
def index(user):
    v = DB.query('title', 'type').filter(Article.id == 1000002).one()
    print(v[0])

    return jsonify({
          'code': 200,
          'msg': {
                'user': user
          }
    })


@app.route('/index')
def index2():
    return jsonify({
          'code': 200,
          'msg': {
                'user': 'abbbb'
          }
    })

