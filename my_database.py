from flaskext.mysql import MySQL


# MyDatabase digunakan sebagai class pembantu untuk melakukan command SQL ke Database
class MyDatabase:
    mysql = MySQL()
    conn = None
    cursor = None

    # Fungsi ini digunakan untuk membuat koneksi ke Server MySQL
    @staticmethod
    def connect():
        MyDatabase.conn = MyDatabase.mysql.connect()  # Buka koneksi SQL
        MyDatabase.cursor = MyDatabase.conn.cursor()  # Dapatkan kursor dari koneksi SQL tersebut

    # Fungsi ini digunakan untuk memutuskan koneksi Server MySQL
    @staticmethod
    def disconnect():
        MyDatabase.conn.close()  # Tutup Koneksi SQL
        MyDatabase.cursor = None  # Hapus cursor yang tidak dipakai lagi

    # Fungsi ini digunakan untuk melakukan eksekusi kode SQL seperti CREATE, UPDATE, ataupun DELETE
    @staticmethod
    def execute_and_commit(sql, values=None):
        MyDatabase.connect()  # Buka Koneksi ke database
        MyDatabase.cursor.execute(sql, values)  # Memasukan command SQL pada cursor
        MyDatabase.conn.commit()  # Eksekusi command SQL tersebut
        MyDatabase.disconnect()  # Tutup koneksi

    # Fungsi ini digunakan untuk mendapatkan data dari Server MySQL dengan operasi SQL seperti Select
    @staticmethod
    def query(sql, values=None):
        MyDatabase.connect()  # Buka Koneksi ke database
        MyDatabase.cursor.execute(sql, values)  # Memasukan command SQL pada cursor
        result = MyDatabase.cursor.fetchall()  # Eksekusi command SQL tersebut dan terima hasilnya
        MyDatabase.disconnect()  # Tutup koneksi

        return result  # Kembalikan hasil data yang diterima dari database
