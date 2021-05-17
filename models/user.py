class User:
    def __init__(self, user_id, user_name, password, user_gender):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.user_gender = user_gender

    def to_json(self):
        return {"ID": self.user_id, "Nama": self.user_name,
                "Password": self.password, "Jenis Kelamin": self.user_gender}
