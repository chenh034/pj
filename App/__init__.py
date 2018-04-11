from flask import Flask
app = Flask('App')
app.debug = True

from App.config import *
from App.controllers import *
from App.models import *
