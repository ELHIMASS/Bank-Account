from app.models.user_model import User
from app.models.dataBase import sessionLocal

class UserDAL:
    def __init__(self):
        self.session = sessionLocal()

    def get_all(self):
        return self.session.query(User).all()

    def get_by_id(self, id):
        return self.session.query(User).get(id)

    def get_by_name(self, name):
        return self.session.query(User).filter(User.name == name).first()

    def create(self, user):
        self.session.add(user)
        self.session.commit()

    def update(self, user):
        self.session.commit()

    def delete(self, user):
        self.session.delete(user)
        self.session.commit()