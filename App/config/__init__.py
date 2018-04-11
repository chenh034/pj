import os
from configparser import ConfigParser
import glo

CONFIG = {}
cfg = ConfigParser()
cfg.read('App/config/default.conf')

sections = cfg.sections()
for secKey in sections:
    CONFIG[secKey] = {}
    options = cfg.options(secKey)
    for optKey in options:
        CONFIG[secKey][optKey] = cfg.get(secKey, optKey)


if os.environ.get('PYTHON_ENV'):
    if os.environ['PYTHON_ENV'] == 'develop':
        cfg.read('App/config/develop.conf')
    elif os.environ['PYTHON_ENV'] == 'test-internet':
        cfg.read('App/config/test-internet.conf')
    elif os.environ['PYTHON_ENV'] == 'production':
        cfg.read('App/config/production.conf')


sections = cfg.sections()

for secKey in sections:
    if secKey not in CONFIG:
        CONFIG[secKey] = {}
    options = cfg.options(secKey)
    for optKey in options:
        CONFIG[secKey][optKey] = cfg.get(secKey, optKey)

glo.set_value('CONFIG', CONFIG)
