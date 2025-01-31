from app.dal.bankAccount_dal import BankAccountDAL

class BankAccountService:
    def __init__(self):
        self.bankAccount_dal = BankAccountDAL()

    def get_all(self):
        return self.bankAccount_dal.get_all()

    def get_by_id(self, id):
        return self.bankAccount_dal.get_by_id(id)

    def create(self, bankAccount):
        return self.bankAccount_dal.create(bankAccount)

    def update(self, bankAccount):
        return self.bankAccount_dal.update(bankAccount)

    def delete(self, bankAccount):
        return self.bankAccount_dal.delete(bankAccount)