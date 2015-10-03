__author__ = 'niko'
'''
The session is the way SQLAlchemy ORM interacts with the database.
It wraps a database connection via an engine,
and provides an identity map for objects that you load via the session
or associate with the session.
The identity map is a cache like data structure
that contains a unique list of objects determined by the object’s table
and primary key. A session also wraps a transaction,
and that transaction will be open until the Session is committed or rolled back
'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine("postgres://niko:112233@localhost/orm_test_db")
Session=sessionmaker(bind=engine)
session=Session()
