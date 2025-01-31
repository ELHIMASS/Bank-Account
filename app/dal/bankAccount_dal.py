from app.models.bankAcount_model import BankAccount
from app.models.dataBase import sessionLocal

class BankAccountDAL:
    def __init__(self):
        self.session = sessionLocal()

    def get_all(self):
        return self.session.query(BankAccount).all()

    def get_by_id(self, id):
        return self.session.query(BankAccount).get(id)

    def create(self, bankAccount):
        self.session.add(bankAccount)
        self.session.commit()

    def update(self, bankAccount):
        self.session.commit()

    def delete(self, bankAccount):
        self.session.delete(bankAccount)
        self.session.commit()