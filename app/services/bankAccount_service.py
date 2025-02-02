from app.dal.bankAccount_dal import BankAccountDAL
from typing import Final
from app.services.operation_service import OperationService

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
        if bankAccount.type_compte == "cheking":
            if bankAccount.balance >= self.SAVING_AMOUNT:
                return "account not created !!!, Balance should be greater than 100"
            else:
                return self.bankAccount_dal.create(bankAccount)   
        return self.bankAccount_dal.create(bankAccount)

    def update(self, bankAccount):
        return self.bankAccount_dal.update(bankAccount)

    def delete(self, bankAccount):
        return self.bankAccount_dal.delete(bankAccount)
