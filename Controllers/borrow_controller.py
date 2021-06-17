from my_database import MyDatabase
from Models.borrow import Borrow


# Sebuah Controller untuk mengakses Tabel borrow pada database library_0082
class BorrowController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel borrow dalam database library_0082
    @staticmethod
    def insert(borrow):
        MyDatabase.execute_and_commit(
            "INSERT into borrow VALUES(%s, %s, %s, %s, %s, %s)",
            [borrow.borrow_id, borrow.book_id, borrow.username, borrow.secret_key, borrow.borrow_date,
             borrow.return_date]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel borrow dalam database library_0082
    @staticmethod
    def update(borrow):
        MyDatabase.execute_and_commit(
            "UPDATE borrow SET book_id=%s, username=%s, secret_key=%s, borrow_date=%s, return_date=%s WHERE borrow_id=%s",
            [borrow.book_id, borrow.username, borrow.secret_key, borrow.borrow_date, borrow.return_date,
             borrow.borrow_id]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel borrow dalam database library_0082 berdasarkan borrow_id
    @staticmethod
    def delete(borrow_id):
        MyDatabase.execute_and_commit(
            "DELETE FROM borrow where borrow_id=%s",
            [borrow_id]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel borrow dalam database library_0082
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM borrow")

        # Setiap hasil data borrow dari database library_0082 disimpan ke dalam model borrow
        list_borrow = []
        for borrow in hasil:
            list_borrow += [Borrow(*borrow)]

        return list_borrow

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel borrow dalam database library_0082 berdasarkan borrow_id
    @staticmethod
    def get_by_id(borrow_id):
        hasil = MyDatabase.query(
            "SELECT * FROM borrow where borrow_id=%s",
            [borrow_id]
        )

        m = None
        # Jika borrow_id tersebut berhasil ditemukan
        if hasil:
            borrow = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = Borrow(*borrow)

        return m
