import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from db import Product , Option, Unit, session, Category, Supplier

class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        price = graphene.Int(required=True)
        stock = graphene.Int()
        buy = graphene.Int()
        category_id = graphene.Int(required=True)
        supplier_id = graphene.Int(required=True)
        
    product = graphene.Field(Product)
    
    def mutate(self, info, name, price, category_id, supplier_id, description=None,  stock=None, buy=None):
        product = Product(name=name, description=description, price=price, stock=stock, buy=buy, category_id=category_id, supplier_id=supplier_id)
        session.add(product)
        session.commit()
        return CreateProduct(product=product)
    
    
class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        description = graphene.String()
        price = graphene.Int()
        stock = graphene.Int()
        buy = graphene.Int()
        category_id = graphene.Int()
        supplier_id = graphene.Int()
        
    product = graphene.Field(Product)
    
    def mutate(self, info, id, name=None, description=None, price=None, stock=None, buy=None, category_id=None, supplier_id=None):
        product = session.query(Product).filter(Product.id == id).first()
        if product:
            if name:
                product.name = name
            if description:
                product.description = description
            if price:
                product.price = price
            if stock is not None:
                product.stock = stock
            if buy is not None:
                product.buy = buy
            if category_id:
                product.category_id = category_id
            if supplier_id:
                product.supplier_id = supplier_id
                
            session.commit()
            
        return UpdateProduct(product=product)
    
    
class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        
    product_id = graphene.Int()
    
    def mutate(self, info, id):
        product = session.query(Product).filter(Product.id == id).first()
        
        if product:
            session.delete(product)
            session.commit()
            return DeleteProduct(product_id=id)
        
        return None
    
