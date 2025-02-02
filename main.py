
"""from app.controlers.user_controler import user
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

#app = create_app()



Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User {self.name}>"
    
if __name__ == '__main__':
    #user=app.register_blueprint(user, url_prefix='')
    #app.run(debug=True)
    engine = create_engine('mysql+mysqlconnector://root:@localhost/db_bank')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(User(name='admin', password='admin', is_admin=True))
    session.add(User(name='user', password='user', is_admin=False))
    session.commit()

    # Récupère tous les utilisateurs
    users = session.query(User).all()
    for user in users:
        print(user)
"""
from flask import Flask,render_template,Blueprint
from app.controlers.user_controler import user 
from app.controlers.BankAccount_controller import bankAccount
from app.controlers.operation_controler import operation
from app import app
from app.models.user_model import User
from app.models.operation_model import  Base
from app.models.dataBase import engine
import secrets
from app.services.bankAccount_service import BankAccountService

def create_tables():
    try:
        # Crée toutes les tables
        Base.metadata.create_all(bind=engine)
        print("Tables créées avec succès !")
    except Exception as e:
        print(f"Erreur lors de la création des tables : {e}")

if __name__ == '__main__':
    create_tables()
    b = BankAccountService()
    print(b.get_cheking())
    
    