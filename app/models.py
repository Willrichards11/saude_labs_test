from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import create_app


app = create_app()
database = SQLAlchemy(app)


class Orders(database.Model):
    """A database model to for the sqlite database orders table """
    id = Column(Integer, primary_key=True)
    created_at = Column(String(10))
    customer_id = Column(Integer, nullable=False)
    vendor_id = Column(Integer, nullable=False)


class Commissions(database.Model):
    """ A database model to for the sqlite database Commissions table"""
    key = Column(Integer, primary_key=True)
    date = Column(String(10))
    rate = Column(Float)
    vendor_id = Column(Integer)


class ProductPromotions(database.Model):
    """ A database model to for the sqlite database Product_Promotions table"""
    key = Column(Integer, primary_key=True)
    date = Column(String(10))
    product_id = Column(Integer)
    promotion_id = Column(Integer)


class Promotions(database.Model):
    """ A database model to for the sqlite database Promotions table"""
    id = Column(Integer, primary_key=True)
    description = Column(String(100))


class Products(database.Model):
    """ A database model to for the sqlite database Products table"""
    id = Column(Integer, primary_key=True)
    description = Column(String(100))


class OrderLines(database.Model):
    """ A database model to for the sqlite database OrderLines table"""
    key = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    product_id = Column(Integer)
    product_description = Column(String(100))
    product_price = Column(Integer)
    product_vat_rate = Column(Float)
    discount_rate = Column(Float)
    quantity = Column(Integer)
    full_price_amount = Column(Integer)
    discounted_amount = Column(Integer)
    vat_amount = Column(Float)
    total_amount = Column(Float)
