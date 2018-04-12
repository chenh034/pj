import glo
from flask import jsonify
from App import app
from gevent import monkey

from App.models.article import Article

monkey.patch_all()

DB = glo.get_value('DB')
ENGINE = glo.get_value('ENGINE')


@app.route('/test/<int:user>')
def index(user):
    v = DB.query(Article).filter(Article.id == 1000002).one().to_dict()

    return jsonify({
          'code': 200,
          'msg': {
                'data': v
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

