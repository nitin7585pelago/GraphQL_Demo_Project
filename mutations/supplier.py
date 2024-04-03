import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from db import Product , Option, Unit, session, Category, Supplier

class CreateSupplier(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        contact_person = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        
    supplier = graphene.Field(Supplier)
    
    def mutate(self, info, name, contact_person, email, phone):
        supplier = Supplier(name=name, contact_person=contact_person, email=email, phone=phone)
        session.add(supplier)
        session.commit()
        return CreateSupplier(supplier=supplier)
    
    
class UpdateSupplier(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        contact_person = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        
    supplier = graphene.Field(Supplier)
    
    def mutate(self, info, id, name=None, contact_person=None, email=None, phone=None):
        supplier = session.query(Supplier).filter(Supplier.id == id).first()
        
        if supplier:
            if name:
                supplier.name = name
            if contact_person:
                supplier.contact_person = contact_person
            if email:
                supplier.email = email
            if phone:
                supplier.phone = phone
            session.commit()
            
        return UpdateSupplier(supplier=supplier)
    
    
class DeleteSupplier(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        
    supplier_id = graphene.Int()
    
    def mutate(self, info, id):
        supplier = session.query(Supplier).filter(Supplier.id == id).first()
        
        if supplier:
            session.delete(supplier)
            session.commit()
            return DeleteSupplier(supplier_id=id)
        
        return None