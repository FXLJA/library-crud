# Class ini digunakan untuk menyimpan data Borrow dari database library_0082
class Borrow:
    # Constructor ini digunakan untuk inisialiasi data dari class Borrow
    def __init__(self, borrow_id, book_id, username, secret_key, borrow_date, return_date):
        self.borrow_id = borrow_id
        self.book_id = book_id
        self.username = username
        self.secret_key = secret_key
        self.borrow_date = borrow_date
        self.return_date = return_date
