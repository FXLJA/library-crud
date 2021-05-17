from models.book import Book
from dbController import DBController


class BookController:
    @staticmethod
    def insert(book: Book):
        DBController.execute_and_commit(
            "INSERT INTO book VALUES(%s, %s, %s, %s, %s, %s)",
            [book.book_id, book.title, book.author, book.thumbnail, book.file_path, book.book_category]
        )

    @staticmethod
    def update(book: Book):
        DBController.execute_and_commit(
            "UPDATE book SET "
            "title = %s, "
            "author = %s, "
            "thumbnail = %s, "
            "file_path = %S, "
            "book_category = %s "
            "WHERE book_id = %s",
            [book.title, book.author, book.thumbnail, book.file_path, book.book_category, book.book_id]
        )

    @staticmethod
    def delete(book_id):
        DBController.execute_and_commit(
            "DELETE FROM book WHERE book_id = %s",
            [book_id]
        )

    @staticmethod
    def getAll():
        result = DBController.query("SELECT * FROM book")
        books = []

        for book in result:
            b = Book(book[0], book[1], book[2], book[3], book[4], book[5])
            books += [b]

        return books

    @staticmethod
    def getByID(book_id):
        result = DBController.query(
            "SELECT * FROM book WHERE book_id = %s",
            [book_id]
        )
        b = None
        if result:
            book = result[0]
            b = Book(book[0], book[1], book[2], book[3], book[4], book[5])
        return b
