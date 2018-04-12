from flask import Flask
from App.middlewares.fault import FaultWrapper

app = Flask('App')
app.wsgi_app = FaultWrapper(app.wsgi_app)
app.debug = True

from App.config import *
from App.controllers import *
import App.models
