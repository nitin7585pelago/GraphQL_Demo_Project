import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from db import Product as ProductModel, Option as OptionModel, Unit as UnitModel, session


class ProductType(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel


class OptionType(SQLAlchemyObjectType):
    class Meta:
        model = OptionModel


class UnitType(SQLAlchemyObjectType):
    class Meta:
        model = UnitModel


class QueryType(graphene.ObjectType):
    products = graphene.List(ProductType)
    options = graphene.List(OptionType)
    units = graphene.List(UnitType)
    
    def resolve_products(self, info):
        return ProductModel.query.all()
    
    def resolve_options(self, info):
        return OptionModel.query.all()
    
    def resolve_units(self, info):
        return UnitModel.query.all()


class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
    
    product = graphene.Field(ProductType)
    
    def mutate(self, info, name, description=None):
        product = ProductModel(name=name, description=description)
        session.add(product)
        session.commit()
        return CreateProduct(product=product)


class MutationType(graphene.ObjectType):
    create_product = CreateProduct.Field()
    
    
schema = graphene.Schema(query=QueryType, mutation=MutationType)