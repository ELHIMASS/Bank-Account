from app import Base
from sqlalchemy import Column, Integer, String, Boolean
class User(Base):
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "is_admin": self.is_admin
        }
