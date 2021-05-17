class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_json(self):
        return {"Username": self.username, "Password": self.password}

    @staticmethod
    def get_types():
        return ["str", "str"]
