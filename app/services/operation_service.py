from app.dal.operation_dal import OperationDAL
from app.models.bankAcount_model import BankAccount
from app.models.operation_model import Operation
from app.models.dataBase import sessionLocal


class OperationService:
    def __init__(self):
        self.operation_dal = OperationDAL()

    def get_all(self):
        return self.operation_dal.get_all()

    def get_by_id(self, id):
        return self.operation_dal.get_by_id(id)

    def create(self, operation):
        return self.operation_dal.create(operation)

    def create_transfer(self, sender_id, receiver_id, amount):
        return self.operation_dal.create_transfer(sender_id, receiver_id, amount)
    
    def create_deposit(self, account_id, amount):
        return self.operation_dal.create_deposit(account_id, amount)
    
    def create_retirer(self, account_id, amount):
        return self.operation_dal.create_retirer(account_id, amount)
    
    #def search_accounts(self, account_id=None, account_type=None, min_balance=None, max_balance=None):
        #"""Recherche des comptes avec des filtres dynamiques"""
        #return self.bankAccount_dal.search(account_id, account_type, min_balance, max_balance)
    
    def get_operations_by_account(self, account_id):
        """Récupère toutes les opérations d'un compte donné"""
        return self.operation_dal.get_operations_by_account(account_id)
    
    
    def update(self, operation):
        return self.operation_dal.update(operation)

    def delete(self, operation):
        return self.operation_dal.delete(operation)  
    
    
    def get_all_accounts_by_user(self, user_id):
        db_session = sessionLocal()
        try:
            return db_session.query(BankAccount).filter_by(user_id=user_id).all()
        finally:
            db_session.close()
  
    
    
  