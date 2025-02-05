from sqlalchemy import String, Column, Integer, Float, Enum, ForeignKey
from app import Base
from sqlalchemy.orm import relationship
from app.models.bankAcount_model import BankAccount

class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bank_account_id = Column(Integer, ForeignKey('bank_accounts.id'))
    type_operation = Column(Enum('deposit', 'withdraw', 'transfer', name='operation_type'), nullable=False)
    amount = Column(Float, nullable=False)
    sender_account_id = Column(Integer, ForeignKey('bank_accounts.id', ondelete='SET NULL'), nullable=True)
    receiver_account_id = Column(Integer, ForeignKey('bank_accounts.id', ondelete='SET NULL'), nullable=True)

    # Ajout des relations
    bank_account = relationship('BankAccount', foreign_keys=[bank_account_id], back_populates='operations')
    sender_account = relationship('BankAccount', foreign_keys=[sender_account_id], back_populates='sent_operations')
    receiver_account = relationship('BankAccount', foreign_keys=[receiver_account_id], back_populates='received_operations')

    def __repr__(self):
        return f"<Operation id :{self.id} bank_account_id :{self.bank_account_id} type_operation :{self.type_operation} amount :{self.amount} sender_account_id :{self.sender_account_id} receiver_account_id :{self.receiver_account_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "bank_account_id": self.bank_account_id,
            "type_operation": self.type_operation,
            "amount": self.amount,
            "sender_account_id": self.sender_account_id,
            "receiver_account_id": self.receiver_account_id
        }