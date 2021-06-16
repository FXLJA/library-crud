from my_database import MyDatabase
from Models.book import Book


# Sebuah Controller untuk mengakses Tabel book pada database library_0082
class BookController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel book dalam database library_0082
    @staticmethod
    def insert(book):
        MyDatabase.execute_and_commit(
            "INSERT into book VALUES(%s, %s, %s, %s, %s, %s)",
            [ book.book_id, book.title, book.author, book.thumbnail, book.file_path, book.category_id ]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel book dalam database library_0082
    @staticmethod
    def update(book):
        MyDatabase.execute_and_commit(
            "UPDATE book SET title=%s, author=%s, thumbnail=%s, file_path=%s, category_id=%s WHERE book_id=%s",
            [ book.title, book.author, book.thumbnail, book.file_path, book.category_id, book.book_id]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel book dalam database library_0082 berdasarkan book_id
    @staticmethod
    def delete(book_id):
        MyDatabase.execute_and_commit(
            "DELETE FROM book where book_id=%s",
            [ book_id ]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel book dalam database library_0082
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM book")

        # Setiap hasil data book dari database library_0082 disimpan ke dalam model book
        list_book = []
        for book in hasil:
            list_book += [ Book(*book) ]

        return list_book

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel book dalam database library_0082 berdasarkan book_id
    @staticmethod
    def get_by_id(book_id):
        hasil = MyDatabase.query(
            "SELECT * FROM book where book_id=%s",
            [ book_id ]
        )

        m = None
        # Jika book_id tersebut berhasil ditemukan
        if hasil:
            book = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = Book(*book)

        return m
