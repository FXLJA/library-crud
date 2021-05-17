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
