from models.admin import Admin
from dbController import DBController


class AdminController:
    def insert(self, admin: Admin):
        DBController.execute_and_commit(
            "INSERT INTO admin VALUES(%s, %s)",
            [admin.username, admin.password]
        )

    def update(self, admin: Admin):
        DBController.execute_and_commit(
            "UPDATE admin SET password = %s WHERE username = %s",
            [admin.password, admin.username]
        )

    def delete(self, username):
        DBController.execute_and_commit(
            "DELETE FROM admin WHERE user_id = %s",
            [username]
        )

    def getAll(self):
        result = DBController.query("SELECT * FROM admin")
        admins = []

        for admin in result:
            a = Admin(admin[0], admin[1])
            admins += [a]

        return admins

    def getByID(self, username):
        result = DBController.query(
            "SELECT * FROM admin WHERE username = %s",
            [username]
        )
        a = None
        if result:
            admin = result[0]
            a = Admin(admin[0], admin[1])
        return a
