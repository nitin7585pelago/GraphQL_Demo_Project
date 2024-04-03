import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from db import Product , Option, Unit, session, Category, Supplier
from mutations.product import *
from mutations.catagory import *
from mutations.option import *
from mutations.supplier import *
from mutations.unit import *

class Product(SQLAlchemyObjectType):
    class Meta:
        model = Product
        
        
class Option(SQLAlchemyObjectType):
        
        
class Option(SQLAlchemyObjectType):
    class Meta:
        model = Option
        
        
class Unit(SQLAlchemyObjectType):
        
        
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


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    create_option = CreateOption.Field()
    update_option = UpdateOption.Field()
    delete_option = DeleteOption.Field()
    create_unit = CreateUnit.Field()
    update_unit = UpdateUnit.Field()
    delete_unit = DeleteUnit.Field()
    create_supplier = CreateSupplier.Field()
    update_supplier = UpdateSupplier.Field()
    delete_supplier = DeleteSupplier.Field()
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query, mutation=Mutation)