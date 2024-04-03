import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from db import Unit, session


class CreateUnit(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        abbreviation = graphene.String(required=True)
        product_id = graphene.Int(required=True)
        
    unit = graphene.Field(Unit)
    
    def mutate(self, info, name, abbreviation, product_id):
        unit = Unit(name=name, abbreviation=abbreviation, product_id=product_id)
        session.add(unit)
        session.commit()
        return CreateUnit(unit=unit)
    
    
class UpdateUnit(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        abbreviation = graphene.String()
        product_id = graphene.Int()
        
    unit = graphene.Field(Unit)
    
    def mutate(self, info, id, name=None, abbreviation=None, product_id=None):
        unit = session.query(Unit).filter(Unit.id == id).first()
    
        if unit:
            if name:
                unit.name = name
            if abbreviation:
                unit.abbreviation = abbreviation
            if product_id:
                unit.product_id = product_id
            session.commit()
            
        return UpdateUnit(unit=unit)
    
    
class DeleteUnit(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        
    unit_id = graphene.Int()
    
    def mutate(self, info, id):
        unit = session.query(Unit).filter(Unit.id == id).first()
        
        if unit:
            session.delete(unit)
            session.commit()
            return DeleteUnit(unit_id=id)
        
        return None