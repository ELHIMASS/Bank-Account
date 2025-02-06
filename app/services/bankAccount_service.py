from app.dal.bankAccount_dal import BankAccountDAL
from typing import Final



class BankAccountService:
    SAVING_AMOUNT: Final[float]     = 100
    FREE_TRANSACTIONS:Final[int]    = 3
    TRANSACTION_FEE:Final[float]    = 0.2
    DRAFT_OVER:Final[float]         = 500


    def __init__(self):
        self.bankAccount_dal = BankAccountDAL()

    def get_all(self):
        return self.bankAccount_dal.get_saving()
    
    def get_saving(self):
        return self.bankAccount_dal.get_saving()

    def get_cheking(self):
        return self.bankAccount_dal.get_all()
    
    def get_by_id(self, id):
        return self.bankAccount_dal.get_by_id(id)

    def create(self, bankAccount):
        
        if bankAccount.type_compte == "saving" and bankAccount.balance < self.SAVING_AMOUNT:
            return "Compte épargne non créé ! Le solde doit être supérieur à 100."
        return self.bankAccount_dal.create(bankAccount)
    def update_amount(self,bankAccount, amount):
        return self.bankAccount_dal.update_amount(bankAccount, amount)

    def delete(self, bankAccount):
        return self.bankAccount_dal.delete(bankAccount)
