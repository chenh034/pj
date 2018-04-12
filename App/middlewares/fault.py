import json
import traceback
import webob
import webob.dec
import glo


class Fault(object):
    def __init__(self, error, traceback):
        self.error = error
        self.traceback = traceback

    @webob.dec.wsgify
    def __call__(self, req):
        conf = glo.get_value('CONFIG')

        error = {
            'code': getattr(self.error, 'errcode', 500),
            'desc': str(self.error),
            'msg': {}
        }

        status_code = int(getattr(self.error, 'status_code', 500))
        if status_code == 500:
            if int(conf['db']['echo']):
                print(self.traceback)

        response = webob.Response()
        response.status_int = status_code
        response.content_type = 'application/json'
        response.unicode_body = json.dumps(error)
        return response


class FaultWrapper(object):
    def __init__(self, app):
        self.app = app

    @webob.dec.wsgify
    def __call__(self, req):
        try:
            print(req)
            resp = req.get_response(self.app)
            return resp
        except Exception as e:
            tb = traceback.format_exc()
            return Fault(e, tb)
