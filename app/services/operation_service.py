from app.dal.operation_dal import OperationDAL


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

    def update(self, operation):
        return self.operation_dal.update(operation)

    def delete(self, operation):
        return self.operation_dal.delete(operation)    