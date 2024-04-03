import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from db import Product , Option, Unit, session, Category, Supplier


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        
    category = graphene.Field(Category)
    
    def mutate(self, info, name, description=None):
        category = Category(name=name, description=description)
        session.add(category)
        session.commit()
        return CreateCategory(category=category)
    
    
class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        description = graphene.String()
        
    category = graphene.Field(Category)
    
    def mutate(self, info, id, name=None, description=None):
        category = session.query(Category).filter(Category.id == id).first()
        if category:
            if name:
                category.name = name
            if description:
                category.description = description
            session.commit()
        return UpdateCategory(category=category)
    
    
class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        
    category_id = graphene.Int()
    
    def mutate(self, info, id):
        category = session.query(Category).filter(Category.id == id).first()
        if category:
            session.delete(category)
            session.commit()
            return DeleteCategory(category_id=id)
        return None