from sqlalchemy import Column, Integer, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app import Base

class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=True)
    type_compte = Column(Enum('cheking', 'Saving', name='account_type'), nullable=False)
    
    # Clé étrangère vers l'utilisateur
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    # Relation avec l'utilisateur
    user = relationship(
        "User",
        back_populates="bank_accounts",
        foreign_keys=[user_id]
    )

    # Nouvelle relation pour les opérations (déclarée ici)
    operations = relationship(
        "Operation",
        back_populates="bank_account",  # Lien inverse dans 'Operation'
        foreign_keys="[Operation.bank_account_id]",
        cascade="all, delete-orphan"
    )

    # Relation avec les opérations envoyées et reçues
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
