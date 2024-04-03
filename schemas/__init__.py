import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from db import Product, Option, Unit, session, Category, Supplier

class Product(SQLAlchemyObjectType):
    class Meta:
        model = Product
        
        
class Option(SQLAlchemyObjectType):
    class Meta:
        model = Option
        
        
class Unit(SQLAlchemyObjectType):
    class Meta:
        model = Unit
        
        
class Category(SQLAlchemyObjectType):
    class Meta:
        model = Category
        
        
class Supplier(SQLAlchemyObjectType):
    class Meta:
        model = Supplier
        
        
class Query(graphene.ObjectType):
    all_products = graphene.List(Product)
    all_options = graphene.List(Option)
    all_units = graphene.List(Unit)
    all_categories = graphene.List(Category)
    all_suppliers = graphene.List(Supplier)
    product = graphene.Field(Product, id=graphene.Int())
    option = graphene.Field(Option, id=graphene.Int())
    unit = graphene.Field(Unit, id=graphene.Int())
    category = graphene.Field(Category, id=graphene.Int())
    supplier = graphene.Field(Supplier, id=graphene.Int())
    
    def resolve_all_products(self, info):
        return session.query(Product).all()
    
    def resolve_all_options(self, info):
        return session.query(Option).all()
    
    def resolve_all_units(self, info):
        return session.query(Unit).all()
    
    def resolve_all_categories(self, info):
        return session.query(Category).all()
    
    def resolve_all_suppliers(self, info):
        return session.query(Supplier).all()
    
    def resolve_product(self, info, id):
        return session.query(Product).filter(Product.id == id).first()
    
    def resolve_option(self, info, id):
        return session.query(Option).filter(Option.id == id).first()
    
    def resolve_unit(self, info, id):
        return session.query(Unit).filter(Unit.id == id).first()
    
    def resolve_category(self, info, id):
        return session.query(Category).filter(Category.id == id).first()
    
    def resolve_supplier(self, info, id):
        return session.query(Supplier).filter(Supplier.id == id).first()


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
    
    
class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)