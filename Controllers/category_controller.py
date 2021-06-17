from my_database import MyDatabase
from Models.category import Category


# Sebuah Controller untuk mengakses Tabel category pada database library_0082
class CategoryController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel category dalam database library_0082
    @staticmethod
    def insert(category):
        MyDatabase.execute_and_commit(
            "INSERT into category VALUES(%s, %s)",
            [category.category_id, category.category_name]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel category dalam database library_0082
    @staticmethod
    def update(category):
        MyDatabase.execute_and_commit(
            "UPDATE category SET category_name=%s WHERE category_id=%s",
            [category.category_name, category.category_id]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel category dalam database library_0082 berdasarkan category_id
    @staticmethod
    def delete(category_id):
        MyDatabase.execute_and_commit(
            "DELETE FROM category where category_id=%s",
            [category_id]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel category dalam database library_0082
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM category")

        # Setiap hasil data category dari database library_0082 disimpan ke dalam model category
        list_category = []
        for category in hasil:
            list_category += [Category(*category)]

        return list_category

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel category dalam database library_0082 berdasarkan category_id
    @staticmethod
    def get_by_id(category_id):
        hasil = MyDatabase.query(
            "SELECT * FROM category where category_id=%s",
            [category_id]
        )

        m = None
        # Jika category_id tersebut berhasil ditemukan
        if hasil:
            category = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = Category(*category)

        return m
