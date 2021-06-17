from my_database import MyDatabase
from Models.admin import Admin


class AdminController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel admin dalam database library_0082
    @staticmethod
    def insert(admin):
        MyDatabase.execute_and_commit(
            "INSERT into admin VALUES(%s, %s)",
            [admin.username, admin.password]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel admin dalam database library_0082
    @staticmethod
    def update(admin):
        MyDatabase.execute_and_commit(
            "UPDATE admin SET password=%s WHERE username=%s",
            [admin.password, admin.username]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel admin dalam database library_0082 berdasarkan username
    @staticmethod
    def delete(username):
        MyDatabase.execute_and_commit(
            "DELETE FROM admin where username=%s",
            [username]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel admin dalam database library_0082
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM admin")

        # Setiap hasil data admin dari database library_0082 disimpan ke dalam model admin
        list_admin = []
        for admin in hasil:
            list_admin += [Admin(*admin)]

        return list_admin

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel admin dalam database library_0082 berdasarkan username
    @staticmethod
    def get_by_id(username):
        hasil = MyDatabase.query(
            "SELECT * FROM admin where username=%s",
            [username]
        )

        m = None
        # Jika username tersebut berhasil ditemukan
        if hasil:
            admin = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = Admin(*admin)

        return m
