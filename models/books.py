"""
Model data untuk objek buku.
Memiliki atribut sebagai berikut:
1. book_id: identifier unik buku. Pada database atribut ini adalah PRIMARY KEY
2. title: judul buku
3. author: penulis buku
4. book_category: kategori buku. Dipilih dengan combo box
"""


class Books:
    def __init__(self, book_id, title, author, book_category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.book_category = book_category
