from models.category import Category
from dbController import DBController


class CategoryController:
    @staticmethod
    def insert(category: Category):
        DBController.execute_and_commit(
            "INSERT INTO category VALUES(%s, %s)",
            [category.category_id, category.category_name]
        )

    @staticmethod
    def update(category: Category):
        DBController.execute_and_commit(
            "UPDATE category SET category_name = %s WHERE category_id = %s",
            [category.category_name, category.category_id]
        )

    @staticmethod
    def delete(category_id):
        DBController.execute_and_commit(
            "DELETE FROM category WHERE category_id = %s",
            [category_id]
        )

    @staticmethod
    def getAll():
        result = DBController.query("SELECT * FROM category")
        categories = []

        for category in result:
            c = Category(category[0], category[1])
            categories += [c]

        return categories

    @staticmethod
    def getByID(category_id):
        result = DBController.query(
            "SELECT * FROM category WHERE category_id = %s",
            [category_id]
        )
        c = None
        if result:
            category = result[0]
            c = Category(category[0], category[1])
        return c
