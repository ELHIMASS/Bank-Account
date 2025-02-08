from sqlalchemy import Column, Integer, Float, ForeignKey, Enum, DateTime, func
from sqlalchemy.orm import relationship
from app import Base

class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    type = Column(Enum('deposit', 'withdrawal', 'transfer', name='operation_type'), nullable=False)
    date = Column(DateTime, default=func.now(), nullable=False)

    # Clé étrangère pour le compte bancaire (récepteur et expéditeur)
    bank_account_id = Column(Integer, ForeignKey('bank_accounts.id'), nullable=True)
    sender_account_id = Column(Integer, ForeignKey('bank_accounts.id'), nullable=True)
    receiver_account_id = Column(Integer, ForeignKey('bank_accounts.id'), nullable=True)

    
    bank_account = relationship(
        "BankAccount",
        back_populates="operations",  
        foreign_keys=[bank_account_id]
    )

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
