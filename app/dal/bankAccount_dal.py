from sqlalchemy import and_
from app.models.user_model import User
from app.models.bankAcount_model import BankAccount
from app.models.operation_model import Operation
from app import sessionLocal

class BankAccountDAL:
    def __init__(self):
        self.session = sessionLocal()

    def get_all(self):
        return self.session.query(BankAccount).all()
    
    def get_saving(self):
        return self.session.query(BankAccount).filter(BankAccount.type_compte == "Saving").all()
    
    def get_cheking(self):
        return self.session.query(BankAccount).filter(BankAccount.type_compte == "cheking").all()

    def get_by_id(self, id):
        return self.session.query(BankAccount).get(id)

    def create(self, bankAccount:BankAccount):
        self.session.add(bankAccount)
        self.session.commit()

    def update(self, bankAccount):
        self.session.commit()

    def update_amount(self, bankAccount, balance):
        bankAccount.balance = bankAccount.balance + balance  
        self.session.commit()  

        
    def delete(self, bankAccount):
        self.session.delete(bankAccount)
        self.session.commit()

    def search_accounts(self, account_id=None, account_type=None, min_balance=None, max_balance=None):
        # Construire la requête de base
        query = self.session.query(BankAccount)

        # Ajouter des filtres dynamiques en fonction des paramètres
        filters = []
        if account_id:
            filters.append(BankAccount.id == account_id)
        if account_type and account_type != "Tous":
            filters.append(BankAccount.type_compte == account_type)
        if min_balance is not None:
            filters.append(BankAccount.balance >= min_balance)
        if max_balance is not None:
            filters.append(BankAccount.balance <= max_balance)

        # Appliquer les filtres si nécessaires
        if filters:
            query = query.filter(and_(*filters))

        # Exécuter la requête et retourner les résultats
        return query.all()
    
    def get_all_accounts_by_user(self, user_id):
        user =  self.session.query(User).filter(User.id == user_id).one_or_none()
        if user:
            return user.bank_accounts
        else:
            return []

    