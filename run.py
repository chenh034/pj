import os
import glo
glo.init()

from App import app


# from gevent.pywsgi import WSGIServer
if __name__ == '__main__':
    # http_server = WSGIServer(('127.0.0.1', 12306), app)
    # http_server.serve_forever()
    port = int(os.environ.get('PORT', 12306))
    app.run('127.0.0.1', port=port)

