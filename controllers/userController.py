from models.user import User
from dbController import DBController


class UserController:
    def insert(self, user: User):
        DBController.execute_and_commit(
            "INSERT INTO user VALUES(%s, %s, %s, %s)",
            [user.user_id, user.user_name, user.password, user.user_gender]
        )

    def update(self, user: User):
        DBController.execute_and_commit(
            "UPDATE user SET user_name = %s, user_gender = %s, password = %s WHERE user_id = %s",
            [user.user_name, user.password, user.user_gender, user.user_id]
        )

    def delete(self, user_id):
        DBController.execute_and_commit(
            "DELETE FROM user WHERE user_id = %s",
            [user_id]
        )

    def getAll(self):
        result = DBController.query("SELECT * FROM user")
        users = []

        for user in result:
            u = User(user[0], user[1], user[2], user[3])
            users += [u]

        return users

    def getByID(self, user_id):
        result = DBController.query(
            "SELECT * FROM user WHERE user_id = %s",
            [user_id]
        )
        u = None
        if result:
            user = result[0]
            u = User(user[0], user[1], user[2], user[3])
        return u
