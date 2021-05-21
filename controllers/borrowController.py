from models.borrow import Borrow
from dbController import DBController


class BorrowController:
    @staticmethod
    def insert(borrow: Borrow):
        DBController.execute_and_commit(
            "INSERT INTO borrow VALUES(%s, %s, %s, %s, %s, %s)",
            [borrow.borrow_id, borrow.book_id, borrow.username,
             borrow.secret_key, borrow.borrow_date, borrow.return_date]
        )

    @staticmethod
    def update(borrow: Borrow):
        DBController.execute_and_commit(
            "UPDATE borrow SET "
            "book_id = %s, "
            "username = %s, "
            "secret_key = %S, "
            "borrow_date = %s "
            "return_date = %s, "
            "WHERE borrow_id = %s",
            [borrow.book_id, borrow.username, borrow.secret_key,
             borrow.borrow_date, borrow.return_date, borrow.borrow_id]
        )

    @staticmethod
    def delete(borrow_id):
        DBController.execute_and_commit(
            "DELETE FROM borrow WHERE borrow_id = %s",
            [borrow_id]
        )

    @staticmethod
    def getAll():
        result = DBController.query("SELECT * FROM borrow")
        borrows = []

        for borrow in result:
            b = Borrow(borrow[0], borrow[1], borrow[2], borrow[3], borrow[4], borrow[5])
            borrows += [b]

        return borrows

    @staticmethod
    def getByID(borrow_id):
        result = DBController.query(
            "SELECT * FROM borrow WHERE borrow_id = %s",
            [borrow_id]
        )
        b = None
        if result:
            borrow = result[0]
            b = Borrow(borrow[0], borrow[1], borrow[2], borrow[3], borrow[4], borrow[5])
        return b
