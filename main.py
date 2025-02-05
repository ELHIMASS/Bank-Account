
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
import secrets



if __name__ == '__main__':
    operation = app.register_blueprint(operation,url_prefix='/operation')
    bankAccount = app.register_blueprint(bankAccount,url_prefix='/compte')
    user=app.register_blueprint(user,url_prefix='/')
    app.secret_key = secrets.token_hex(32)
    app.run(debug=True)
    