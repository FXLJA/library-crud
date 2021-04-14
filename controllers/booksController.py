"""
Class BooksController untuk mengendalikan operasi CRUD yang diterapkan pada model 'books' untuk objek buku.
Class ini mengandung method untuk melakukan query SQL ke dalam database berupa:
1. INSERT INTO untuk menambah data
2. SELECT untuk menampilkan data
3. UPDATE untuk memperbarui data
4. DELETE untuk menghapus data
"""

from models.books import Books
from dbController import DBController


class BooksController:
    def insert(self, buku: Books):
        DBController.execute_and_commit(
            "INSERT INTO books VALUES(%s, %s, %s, %s)",
            [buku.book_id, buku.title, buku.author, buku.book_category]
        )

    def update(self, buku: Books):
        DBController.execute_and_commit(
            "UPDATE books SET title = %s, author = %s, book_category = %s WHERE book_id = %s",
            [buku.title, buku.author, buku.book_category, buku.book_id]
        )

    def delete(self, book_id):
        DBController.execute_and_commit(
            "DELETE FROM books WHERE book_id = %s",
            [book_id]
        )

    def getAll(self):
        result = DBController.query("SELECT * FROM books")
        books = []

        for book in result:
            b = Books(book[0], book[1], book[2], book[3])
            books += [b]

        return books

    def getByID(self, book_id):
        result = DBController.query(
            "SELECT * FROM books WHERE book_id = %s",
            [book_id]
        )
        b = None
        if result:
            book = result[0]
            b = Books(book[0], book[1], book[2], book[3])
        return b
