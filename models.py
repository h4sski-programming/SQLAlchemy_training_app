from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, create_engine, func
from sqlalchemy.orm import declarative_base, relationship, Session
from os import path


db = declarative_base()
DB_NAME = 'database.db'
engine = create_engine(f'sqlite:///{DB_NAME}', echo=True, future=True)
session = Session(engine)


class User(db):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    email = Column(String(200))
    password = Column(String(100))
    full_name = Column(String(150))
    role = Column(String(100), default='member')
    activity = relationship('Activity')


class Activity(db):
    __tablename__ = 'activity'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('user.id'))
    distance = Column(Integer())
    date = Column(Date())
    type = Column(String(100))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


def create_db():
    if not path.exists(f'/{DB_NAME}'):
        db.metadata.create_all(engine)
