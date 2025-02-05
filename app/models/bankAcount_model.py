from sqlalchemy import Column, Integer, String, Float, Enum, rela
from app import Base
from app.models.operation_model import Operation
from sqlalchemy.orm import relationship

class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=True)
    type_compte = Column(Enum('cheking', 'Saving', name='account_type'), nullable=False)
    
    operations = relationship('Operation', foreign_keys='Operation.bank_account_id', back_populates='bank_account')

    def __repr__(self):
        return f"<BankAccount id :{self.id} balance :{self.balance} interest_rate :{self.interest_rate} type_compte :{self.type_compte}>"

    def to_dict(self):
        
        return {
            "id": self.id,
            "balance": self.balance,
            "interest_rate": self.interest_rate,
            "type_compte": self.type_compte
        }
        
