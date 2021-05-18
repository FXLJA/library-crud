class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

    def to_json(self):
        return {"Category ID": self.category_id, "Category Name": self.category_name}

    @staticmethod
    def get_types():
        return ["str", "str"]
