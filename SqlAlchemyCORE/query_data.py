__author__ = 'niko'
from sqlalchemy import select,create_engine

from CreateBasicTable import cookies

engine=create_engine("postgresql://niko:112233@localhost/test")
connection=engine.connect()

rp=engine.execute(select([cookies]))
results=rp.fetchall()
print (results)