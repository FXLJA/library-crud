class Borrow:
    def __init__(self, borrow_id, book_id, username, secret_key, borrow_date, return_date):
        self.borrow_id = borrow_id
        self.book_id = book_id
        self.username = username
        self.secret_key = secret_key
        self.borrow_date = borrow_date
        self.return_date = return_date

    def to_json(self):
        return {"borrow id": self.borrow_id, "book id": self.book_id,
                "username": self.username, "secret key": self.secret_key,
                "borrow date": self.borrow_date, "return date": self.return_date}
