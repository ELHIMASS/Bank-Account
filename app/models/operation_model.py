from sqlalchemy import Column, Integer, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.models.dataBase import Base

class Operation(Base):
    __tablename__ = 'operations'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    bank_account_id = Column(Integer, ForeignKey('bank_accounts.id', ondelete='CASCADE'))
    type_operation = Column(Enum('deposit', 'withdraw', 'transfer', name='operation_type'), nullable=False)
    amount = Column(Float, nullable=False)
    sender_account_id = Column(Integer, ForeignKey('bank_accounts.id', ondelete='SET NULL'), nullable=True)
    receiver_account_id = Column(Integer, ForeignKey('bank_accounts.id', ondelete='SET NULL'), nullable=True)
    # Relation avec BankAccount
    bank_account = relationship(
        "BankAccount",
        back_populates="operations",
        foreign_keys=[bank_account_id]
    )

    # Relations pour les transferts
    sender_account = relationship(
        "BankAccount",
        back_populates="sent_operations",
        foreign_keys=[sender_account_id]
    )

    receiver_account = relationship(
        "BankAccount",
        back_populates="received_operations",
        foreign_keys=[receiver_account_id]
    )