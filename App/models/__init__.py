import glo
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

CONFIG = glo.get_value('CONFIG', {})

s = URL(
    drivername=CONFIG['db']['drivername'],
    username=CONFIG['db']['username'],
    password=CONFIG['db']['password'],
    host=CONFIG['db']['host'],
    port=CONFIG['db']['port'],
    database=CONFIG['db']['database']
)

engine = create_engine(s, echo=int(CONFIG['db']['echo']))

DBSession = sessionmaker(bind=engine)

glo.set_value('ENGINE', engine)
glo.set_value('DB', DBSession())
