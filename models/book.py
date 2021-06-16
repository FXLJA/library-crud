# Class ini digunakan untuk menyimpan data Book dari database library_0082
class Book:
    # Constructor ini digunakan untuk inisialiasi data dari class Book
    def __init__(self, book_id, title, author, thumbnail, file_path, category_id):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.thumbnail = thumbnail
        self.file_path = file_path
        self.category_id = category_id
