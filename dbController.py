"""
Modul pengendali koneksi database. Seluruh method di dalam modul ini bersifat static, karena nilainya tidak akan
mengalami perubahan selama aplikasi dijalankan.

Database yang digunakan adalah MySQL melalui modul ekstensi PyMySQL (pip install pymysql)

Variabel yang digunakan dalam modul ini adalah sebagai berikut:
mysql: instansiasi dari class MySQL, memiliki kapabilitas koneksi database
conn: indikator status koneksi, menjadi perantara dari controller untuk mengubah status koneksi database
cursor: objek yang mampu menulis query ke dalam database, seperti kursor pada text editor
"""

from flaskext.mysql import MySQL


class DBController:
    mysql = MySQL()
    conn = None
    cursor = None

    @staticmethod
    def connect():
        DBController.conn = DBController.mysql.connect()
        DBController.cursor = DBController.conn.cursor()

    @staticmethod
    def disconnect():
        DBController.conn.close()
        DBController.cursor = None

    @staticmethod
    def execute_and_commit(sql, values=None):
        DBController.connect()
        DBController.cursor.execute(sql, values)
        DBController.conn.commit()
        DBController.disconnect()

    @staticmethod
    def query(sql, values=None):
        DBController.connect()
        DBController.cursor.execute(sql, values)
        result = DBController.cursor.fetchall()
        DBController.disconnect()

        return result
