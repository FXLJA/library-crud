# Class ini digunakan untuk menyimpan data User dari database library_0082
class User:
    # Constructor ini digunakan untuk inisialiasi data dari class User
    def __init__(self, username, name, password, gender):
        self.username = username
        self.name = name
        self.password = password
        self.gender = gender
