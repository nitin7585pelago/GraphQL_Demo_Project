from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    String,
    Integer,
    Column,
    ForeignKey,
    Text
)
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = "sqlite:///"+ os.path.join(BASE_DIR, 'inventory.db')

Base = declarative_base()

engine = create_engine(connection_str, echo=True)

session = scoped_session(
    sessionmaker(bind=engine)
)

Base.query = session.query_property()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    buy = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    unit_id = Column(Integer, ForeignKey('units.id'))
    
    category = relationship('Category', back_populates='products')
    supplier = relationship('Supplier', back_populates='products')
    options = relationship('Option', back_populates='products')
    units = relationship('Unit', back_populates='products')
    
    
class Option(Base):
    __tablename__ = 'options'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))
    
    product = relationship('Product', back_populates='options')
    
    
class Unit(Base):
    __tablename__ = 'units'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))
    
    product = relationship('Product', back_populates='units')
    
    
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    
    products = relationship('Product', back_populates='category')
    
    
class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_person = Column(String)
    email = Column(String)
    phone = Column(String)
    
    products = relationship('Product', back_populates='supplier')