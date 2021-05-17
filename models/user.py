class User:
    def __init__(self, user_id, user_name, password, user_gender):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.user_gender = user_gender

    def to_json(self):
        return {"user_id": self.user_id, "user_name": self.user_name,
                "password": self.password, "user_gender": self.user_gender}
