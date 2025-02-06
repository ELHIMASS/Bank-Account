from sqlalchemy import Column, Integer, Float, Enum
from sqlalchemy.orm import relationship
from app.models.dataBase import Base

class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, nullable=False)
    type_compte = Column(Enum('cheking', 'saving', name='account_type'), nullable=False)

    # Relation avec Operation (One-to-Many)
    operations = relationship(
        "Operation",
        back_populates="bank_account",
        foreign_keys="[Operation.bank_account_id]",  # ✅ On spécifie la bonne clé étrangère
        cascade="all, delete-orphan"
    )

    # Relations pour les transferts
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