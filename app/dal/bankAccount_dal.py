from app.models.bankAcount_model import BankAccount
from app.models.dataBase import sessionLocal

class BankAccountDAL:
    def __init__(self):
        self.session = sessionLocal()

    def get_all(self):
        return self.session.query(BankAccount).all()
    
    def get_saving(self):
        return self.session.query(BankAccount).filter(BankAccount.type_compte == "saving").all()
    
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
        query = self.session.query(BankAccount)

        if account_id:
             return self.get_by_id(account_id)
        
        if account_type:
            query = query.filter(BankAccount.type_compte == account_type)
        
        if min_balance is not None:
            query = query.filter(BankAccount.balance >= min_balance)
        
        if max_balance is not None:
            query = query.filter(BankAccount.balance <= max_balance)

        return query.all()
    