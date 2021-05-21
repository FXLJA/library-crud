from flask import url_for
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template
from werkzeug.security import generate_password_hash

from models.admin import Admin
from controllers.adminController import AdminController

TABLE_NAME = "admin"
COL_COUNT = 2

blueprint = Blueprint(TABLE_NAME, __name__, url_prefix=("/" + TABLE_NAME))


@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        item = Admin(*request.form.values())

        if AdminController.getByID(request.form['0']) is not None:
            item = Admin(*([None] * COL_COUNT))
            item_names = item.to_json().keys()
            item_ids = range(COL_COUNT)
            item_types = item.get_types()
            item_arr = [None] * COL_COUNT
            return render_template('crud-default/add.html', message='ID already exists!', table_name=TABLE_NAME,
                                   item=zip(item_names, item_ids, item_types, item_arr))

        item.password = generate_password_hash(item.password)
        AdminController.insert(item)

        return redirect(url_for(TABLE_NAME + '.view'))
    else:
        item = Admin(*([None] * COL_COUNT))
        item_names = item.to_json().keys()
        item_ids = range(COL_COUNT)
        item_types = item.get_types()
        item_arr = [None] * COL_COUNT
        return render_template('crud-default/add.html', table_name=TABLE_NAME,
                               item=zip(item_names, item_ids, item_types, item_arr))


@blueprint.route('/view')
def view():
    return render_template('crud-default/view.html', table_name=TABLE_NAME, items=AdminController.getAll())


@blueprint.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        id = request.form['item_id']
        item = AdminController.getByID(id)

        if item is None:
            item = Admin(*([None] * COL_COUNT))
            item_names = list(item.to_json().keys())
            return render_template('crud-default/update.html', table_name=TABLE_NAME, id_name=item_names[0],
                                   message=(TABLE_NAME + " not found"))

        item.password = ""
        item_names = item.to_json().keys()
        item_values = item.to_json().values()
        item_ids = range(COL_COUNT)
        item_types = item.get_types()
        item_arr = [None] * COL_COUNT

        return render_template('crud-default/UpdateConfirm.html', table_name=TABLE_NAME,
                               item=zip(item_names, item_values, item_ids, item_types, item_arr))

    item = Admin(*([None] * COL_COUNT))
    item_names = list(item.to_json().keys())

    return render_template('crud-default/update.html', table_name=TABLE_NAME, id_name=item_names[0])


@blueprint.route('/update_confirm', methods=['POST'])
def update_confirm():
    item = Admin(*request.form.values())
    item.password = generate_password_hash(item.password)
    AdminController.update(item)
    return redirect(url_for(TABLE_NAME + '.view'))


@blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        id = request.form['item_id']
        item = AdminController.getByID(id)

        if item is None:
            item = Admin(*([None] * COL_COUNT))
            item_names = list(item.to_json().keys())
            return render_template('crud-default/delete.html', table_name=TABLE_NAME, id_name=item_names[0],
                                   message=(TABLE_NAME + " not found"))

        AdminController.delete(id)

        return redirect(url_for(TABLE_NAME + '.view'))

    item = Admin(*([None] * COL_COUNT))
    item_names = list(item.to_json().keys())

    return render_template('crud-default/delete.html', table_name=TABLE_NAME, id_name=item_names[0])