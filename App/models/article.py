from App.models.modelBase import Model
from sqlalchemy import Column
from sqlalchemy.types import Integer, BigInteger, SmallInteger, Float, String, Text

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Model, Base):
    __tablename__ = 'article_tbl'

    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    categoryid = Column(Integer)
    gid = Column(Integer)
    hotgamecid = Column(Integer)
    title = Column(String(255))
    content = Column(Text)
    author = Column(String(20))
    source = Column(String(20))
    cover = Column(String(255))
    intro = Column(String(255))
    timer = Column(BigInteger)
    matchseo = Column(Integer)
    ispublish = Column(Integer)
    createtime = Column(BigInteger)
    updatetime = Column(BigInteger)
    deletetime = Column(BigInteger)
    videolink = Column(String(512))
    images = Column(Text)
    views = Column(Integer)
    praisenum = Column(Integer)
    score = Column(Float)
    url = Column(String(255))
    isoriginal = Column(Integer)
    iscapture = Column(SmallInteger)
    youxinimageview = Column(Integer)
    captureurl = Column(String(512))
    duration = Column(String(10))
    isclips = Column(Integer)
    pagenav = Column(String(255))

