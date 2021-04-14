"""
Class UsersController untuk mengendalikan operasi CRUD yang diterapkan pada model 'users' untuk objek user.
Class ini mengandung method untuk melakukan query SQL ke dalam database berupa:
1. INSERT INTO untuk menambah data
2. SELECT untuk menampilkan data
3. UPDATE untuk memperbarui data
4. DELETE untuk menghapus data
"""

from models.users import Users
from dbController import DBController


class UsersController:
    def insert(self, user: Users):
        DBController.execute_and_commit(
            "INSERT INTO users VALUES(%s, %s, %s, %s)",
            [user.user_id, user.user_name, user.user_gender, user.password]
        )

    def update(self, user: Users):
        DBController.execute_and_commit(
            "UPDATE users SET user_name = %s, user_gender = %s, password = %s WHERE user_id = %s",
            [user.user_name, user.user_gender, user.password, user.user_id]
        )

    def delete(self, user_id):
        DBController.execute_and_commit(
            "DELETE FROM users WHERE user_id = %s",
            [user_id]
        )

    def getAll(self):
        result = DBController.query("SELECT * FROM users")
        users = []

        for user in result:
            u = Users(user[0], user[1], user[2], user[3])
            users += [u]

        return users

    def getByID(self, user_id):
        result = DBController.query(
            "SELECT * FROM users WHERE user_id = %s",
            [user_id]
        )
        u = None
        if result:
            user = result[0]
            u = Users(user[0], user[1], user[2], user[3])
        return u
