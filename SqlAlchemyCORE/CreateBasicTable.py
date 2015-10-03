from sqlalchemy import MetaData,Table,Column,Integer,DateTime,Numeric,String,ForeignKey,Boolean
from datetime import datetime
from sqlalchemy import create_engine




metadata=MetaData()

cookies = Table('cookies',
              metadata,
              Column('cookie_id',Integer(),primary_key=True),
              Column('cookie_name',String(length=50),index=True),
              Column('cookie_recipe_url',String(length=255)),
              Column('cookie_sku',String(length=55)),
              Column('quantity',Integer()),
              Column('unit_cost',Numeric(precision=12,scale=2)))


users = Table('users',metadata,
            Column('user_id',Integer(),primary_key=True),
            Column('username',String(length=15),nullable=False),
            Column('email_address', String(length=255),nullable=False),
            Column('phone',String(length=20),nullable=False),
            Column('password',String(length=25),nullable=False),
            Column('created_on',DateTime(),default=datetime.now),
            Column('updated_on',DateTime(),default=datetime.now(),onupdate=datetime.now)
            )

orders = Table('orders', metadata,
               Column('order_id',Integer(),primary_key=True),
               Column('user_id',Integer(),ForeignKey(column='users.user_id')),
               Column('shipped',Boolean(),default=False))

line_items= Table('line_items',metadata,
                  Column('line_items_id',Integer(),primary_key=True),
                  Column('order_id',Integer(),ForeignKey(column='orders.order_id')),
                  Column('cookie_id',Integer(),ForeignKey(column='cookies.cookie_id')),
                  Column('quantity',Integer()),
                  Column('extended_cost',Numeric(precision=12,scale=2)))

if __name__=="__main__":
    engine = create_engine("postgresql://niko:112233@localhost/test")
    connection = engine.connect()

    metadata=MetaData()

    metadata.create_all(engine)
    print "finished"