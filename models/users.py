"""
Model data untuk objek user.
Memiliki atribut sebagai berikut:
1. user_id: identifier unik user. Pada database atribut ini adalah PRIMARY KEY. Diisi dengan NIM
2. user_name: nama user
3. user_gender: jenis kelamin user. Dipilih dengan radio button
4. password
"""


class Users:
    def __init__(self, user_id, user_name, user_gender, password):
        self.user_id = user_id
        self.user_name = user_name
        self.user_gender = user_gender
        self.password = password
