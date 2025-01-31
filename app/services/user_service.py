from app.dal.user_dal import UserDAL
from app.models.dataBase import sessionLocal

class UserService:
    def __init__(self):
        self.user_dal = UserDAL()

    def get_all(self):
        return self.user_dal.get_all()

    def get_by_id(self, id):
        return self.user_dal.get_by_id(id)

    def get_by_name(self, name):
        return self.user_dal.get_by_name(name)

    def create(self, user):
        return self.user_dal.create(user)

    def update(self, user):
        return self.user_dal.update(user)

    def delete(self, user):
        return self.user_dal.delete(user)