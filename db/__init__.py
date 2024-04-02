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
    options = relationship('Option', back_populates='product')
    
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