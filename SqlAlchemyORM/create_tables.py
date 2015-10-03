__author__ = 'niko'
from  sqlalchemy import ForeignKey,Integer,Boolean,String,Table,Column,create_engine,Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref,relationship,sessionmaker
from datetime import datetime
from sqlalchemy import DateTime


Base = declarative_base()

engine =create_engine("postgres://niko:112233@localhost/orm_test_db",echo=True)
connection=engine.connect()


class Cookie(Base):
    __tablename__='cookies'
    cookie_id = Column(Integer(),primary_key=True)
    cookie_name=Column(String(length=50),index=True)
    cookie_recipe_url= Column(String(length=255))
    cookie_sku=Column(String(length=55))
    quantity = Integer()
    unit_cost= Numeric(precision=12,scale=2)
    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}', " \
                      "cookie_recipe_url='{self.cookie_recipe_url}', " \
                      "cookie_sku='{self.cookie_sku}', " \
                      "quantity={self.quantity}, " \
                      "unit_cost={self.unit_cost})".format(self=self)


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    def __repr__(self):
        return "User(username='{self.username}', " \
                     "email_address='{self.email_address}', " \
                     "phone='{self.phone}', " \
                     "password='{self.password}')".format(self=self)

class Order(Base):
    __tablename__ = 'orders'

    order_id=Column(Integer(),primary_key=True)
    user_id=Column(Integer(),ForeignKey('users.user_id'))
    shipped=Column(Boolean(),default=False)

    # One-To-Many relashionship with User class
    # We can get the User related to this Order
    # by accessing the user property.
    # This relationship also establishes an orders property
    #  on the User class via the backref keyword argument
    #  which is ordered by the order id.
    user=relationship("User",
         backref=backref(name='orders',order_by=order_id))

    def __repr__(self):
        return "Order(user_id={self.user_id}, " \
                    "shipped={self.shipped})".format(self=self)


class LineItem(Base):
    __tablename__ = 'line_items'

    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.order_id'))
    cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))

    #One-to-many relashionship
    order = relationship("Order",
            backref=backref('line_items', order_by=line_item_id))

    #uselist=False keyword argument defines it as a one to one relationship
    cookie = relationship("Cookie", uselist=False)

    def __repr__(self):
        return "LineItems(order_id={self.order_id}, " \
                "cookie_id={self.cookie_id}, " \
                "quantity={self.quantity}, " \
                "extended_cost={self.extended_cost})".format(self=self)

Base.metadata.create_all(engine)
print  "Created database"

#session is the way SQLAlchemy ORM interacts with the database.
#  It wraps a database connection via an engine,
# and provides an identity map for objects
# that you load via the session or associate with the session.
Session=sessionmaker(bind=engine)
sesion=Session()