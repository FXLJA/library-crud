class Borrow:
    def __init__(self, borrow_id, book_id, username, secret_key, borrow_date, return_date):
        self.borrow_id = borrow_id
        self.book_id = book_id
        self.username = username
        self.secret_key = secret_key
        self.borrow_date = borrow_date
        self.return_date = return_date

    def to_json(self):
        return {"ID Peminjaman": self.borrow_id, "ID Buku": self.book_id,
                "Peminjam": self.username, "Kode Pinjam": self.secret_key,
                "Tanggal Pinjam": self.borrow_date, "Tanggal Kembali": self.return_date}

    @staticmethod
    def get_types():
        return ["str", "arr", "arr", "str", "date", "date"]
