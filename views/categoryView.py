from flask import url_for
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from models.category import Category
from controllers.categoryController import CategoryController


blueprint = Blueprint("category", __name__, url_prefix="/category")


@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    # TODO
    return render_template('views/addBooks.html')


@blueprint.route('/view')
def view():
    return render_template('kategori/view.html', table_name="category", items=CategoryController.getAll())


@blueprint.route('/update', methods=['GET', 'POST'])
def update():
    # TODO
    return render_template('views/updateBooks.html')


@blueprint.route('/update_confirm', methods=['POST'])
def update_confirm():
    # TODO
    return redirect(url_for('index'))


@blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    # TODO
    return render_template('views/deleteBooks.html')
