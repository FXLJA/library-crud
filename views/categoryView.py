from flask import url_for
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from models.category import Category
from controllers.categoryController import CategoryController

TABLE_NAME = "category"

blueprint = Blueprint(TABLE_NAME, __name__, url_prefix=("/" + TABLE_NAME))


@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        item = Category(
            request.form['0'],
            request.form['1'],
        )

        if categoryController.getByID(request.form['0']) is not None:
            return render_template('crud-default/add.html', message='ID already exists!')

        categoryController.insert(item)

        return redirect(url_for('index'))
    else:
        c = Category(None, None)
        item_names = c.to_json().keys()
        item_ids = range(2)
        item_types = c.get_types()
        item_arr = [None, None]
        return render_template('crud-default/add.html', table_name=TABLE_NAME ,item=zip(item_names, item_ids, item_types, item_arr))


@blueprint.route('/view')
def view():
    return render_template('crud-default/view.html', table_name=TABLE_NAME, items=CategoryController.getAll())


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
