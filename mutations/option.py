import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from db import Product , Option, Unit, session, Category, Supplier


class CreateOption(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        value = graphene.String(required=True)
        product_id = graphene.Int(required=True)
        
    option = graphene.Field(Option)
    
    def mutate(self, info, name, value, product_id):
        option = Option(name=name, value=value, product_id=product_id)
        session.add(option)
        session.commit()
        return CreateOption(option=option)
    
    
class UpdateOption(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        value = graphene.String()
        product_id = graphene.Int()
        
    option = graphene.Field(Option)
    
    def mutate(self, info, id, name=None, value=None, product_id=None):
        option = session.query(Option).filter(Option.id == id).first()
        
        if option:
            if name:
                option.name = name
            if value:
                option.value = value
            if product_id:
                option.product_id = product_id
            session.commit()
            
        return UpdateOption(option=option)
    
    
class DeleteOption(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        
    option_id = graphene.Int()
    
    def mutate(self, info, id):
        option = session.query(Option).filter(Option.id == id).first()
        
        if option:
            session.delete(option)
            session.commit()
            return DeleteOption(option_id=id)
        
        return None