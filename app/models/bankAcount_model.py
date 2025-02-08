from sqlalchemy import Column, Integer, Float, Enum
from sqlalchemy.orm import relationship
from app.models.dataBase import Base

class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=True)
    type_compte = Column(Enum('cheking', 'Saving', name='account_type'), nullable=False)

    operations = relationship(
        "Operation",
        back_populates="bank_account",
        foreign_keys="[Operation.bank_account_id]", 
        cascade="all, delete-orphan"
    )

    sent_operations = relationship(
        "Operation",
        foreign_keys="[Operation.sender_account_id]",
        back_populates="sender_account"
    )

    received_operations = relationship(
        "Operation",
        foreign_keys="[Operation.receiver_account_id]",
        back_populates="receiver_account"
    )