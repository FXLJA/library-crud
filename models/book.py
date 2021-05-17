"""
Model data untuk objek buku.
Memiliki atribut sebagai berikut:
1. book_id: identifier unik buku. Pada database atribut ini adalah PRIMARY KEY
2. title: judul buku
3. author: penulis buku
4. book_category: kategori buku. Dipilih dengan combo box
"""


class Book:
    def __init__(self, book_id, title, author, thumbnail, file_path, book_category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.thumbnail = thumbnail
        self.file_path = file_path
        self.book_category = book_category
