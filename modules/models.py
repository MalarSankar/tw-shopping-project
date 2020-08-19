from sqlalchemy import Integer,String,Column,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base=declarative_base()

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String(100),nullable=False)
    password=Column(String(10),nullable=False,unique=True)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    items=relationship('Item', backref='Category')

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    seller_id=Column(Integer,ForeignKey('sellers.id'))
    category_id=Column(Integer,ForeignKey('categories.id'))
    carts=relationship('Cart',backref='Item')

class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone_no=Column(Integer,unique=True,nullable=False)

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    item_id=Column(Integer,ForeignKey('items.id'))
    quantity=Column(Integer)






