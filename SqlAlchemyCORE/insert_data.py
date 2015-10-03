from sqlalchemy import MetaData,Table,Column,Integer,DateTime,Numeric,String,ForeignKey,Boolean
from datetime import datetime
from sqlalchemy import create_engine

engine = create_engine("postgresql://niko:112233@localhost/test")
connection = engine.connect()

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

metadata.create_all(engine)
print "finished creating DB, going to store the data\n====================="

ins=cookies.insert().values(cookie_name='choclate chip',
                            cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
                            cookie_sku="CC01",
                            quantity="12",
                            unit_cost="0.50")
print "The insert statement is : "
print(str(ins))

print "==================\nThe parameres in the statement will be replaced by :"
print (ins.compile().params)
print "==================\nExecuting the statement"
result = connection.execute(ins)
print "==================\nResult is "
print result.inserted_primary_key


#Adding several lines at once
#Build our list of cookies.
#Use the list as the second parameter to execute.

inventory_list = [
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
    }
]
result = connection.execute(ins, inventory_list)
