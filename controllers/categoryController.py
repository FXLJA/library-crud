from models.category import Category
from dbController import DBController


class AdminController:
    def insert(self, category: Category):
        DBController.execute_and_commit(
            "INSERT INTO category VALUES(%s, %s)",
            [category.category_id, category.category_name]
        )

    def update(self, category: Category):
        DBController.execute_and_commit(
            "UPDATE category SET category_name = %s WHERE category_id = %s",
            [category.category_name, category.category_id]
        )

    def delete(self, category_id):
        DBController.execute_and_commit(
            "DELETE FROM category WHERE category_id = %s",
            [category_id]
        )

    def getAll(self):
        result = DBController.query("SELECT * FROM category")
        categories = []

        for category in result:
            c = Category(category[0], category[1])
            categories += [c]

        return categories

    def getByID(self, category_id):
        result = DBController.query(
            "SELECT * FROM category WHERE category_id = %s",
            [category_id]
        )
        a = None
        if result:
            category = result[0]
            c = Category(category[0], category[1])
        return c
