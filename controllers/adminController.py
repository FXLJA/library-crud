from models.admin import Admin
from dbController import DBController


class AdminController:
    @staticmethod
    def insert(admin: Admin):
        DBController.execute_and_commit(
            "INSERT INTO admin VALUES(%s, %s)",
            [admin.username, admin.password]
        )

    @staticmethod
    def update(admin: Admin):
        DBController.execute_and_commit(
            "UPDATE admin SET password = %s WHERE username = %s",
            [admin.password, admin.username]
        )

    @staticmethod
    def delete(username):
        DBController.execute_and_commit(
            "DELETE FROM admin WHERE username = %s",
            [username]
        )

    @staticmethod
    def getAll():
        result = DBController.query("SELECT * FROM admin")
        admins = []

        for admin in result:
            a = Admin(admin[0], admin[1])
            admins += [a]

        return admins

    @staticmethod
    def getByID(username):
        result = DBController.query(
            "SELECT * FROM admin WHERE username = %s",
            [username]
        )
        a = None
        if result:
            admin = result[0]
            a = Admin(admin[0], admin[1])
        return a
