from flask import url_for
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

import string
import random
from datetime import datetime

from models.borrow import Borrow
from controllers.bookController import BookController
from controllers.userController import UserController
from controllers.borrowController import BorrowController

TABLE_NAME = "borrow"
COL_COUNT = 6

blueprint = Blueprint(TABLE_NAME, __name__, url_prefix=("/" + TABLE_NAME))


@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    list_user = UserController.getAll()
    list_book = BookController.getAll()
    secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    if request.method == 'POST':
        item = Borrow(*request.form.values())

        if BorrowController.getByID(request.form['borrow_id']) is not None:
            return render_template('borrow/add.html', message='Duplicate order ID', table_name=TABLE_NAME,
                                   list_user=list_user, list_book=list_book, secret_key=secret_key)

        tgl_pinjam = datetime.fromisoformat(item.borrow_date)
        tgl_kembali = datetime.fromisoformat(item.return_date)

        if tgl_kembali < tgl_pinjam:
            return render_template('borrow/add.html', message='Masukkan tanggal yang benar!', table_name=TABLE_NAME,
                                   list_user=list_user, list_book=list_book, secret_key=secret_key)

        BorrowController.insert(item)

        return redirect(url_for(TABLE_NAME + '.view'))

    return render_template('borrow/add.html', table_name=TABLE_NAME, list_user=list_user, list_book=list_book,
                           secret_key=secret_key)


@blueprint.route('/view')
def view():
    items = []

    list_borrow = BorrowController.getAll()
    list_user = UserController.getAll()
    list_book = BookController.getAll()

    for borrow in list_borrow:
        item = {}

        item["borrow_id"] = borrow.borrow_id
        item["secret_key"] = borrow.secret_key
        item["borrow_date"] = borrow.borrow_date
        item["return_date"] = borrow.return_date

        for book in list_book:
            if borrow.book_id == book.book_id:
                item["book_name"] = book.title

        for user in list_user:
            if borrow.username == user.user_id:
                item["user_name"] = user.user_name

        items.append(item)

    return render_template('borrow/view.html', table_name=TABLE_NAME, items=items)


@blueprint.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        id = request.form['item_id']
        item = BorrowController.getByID(id)

        if item is None:
            return render_template('borrow/update.html', table_name=TABLE_NAME, id_name="Borrow ID",
                                   message=(TABLE_NAME + " not found"))

        list_user = UserController.getAll()
        list_book = BookController.getAll()

        return render_template('borrow/UpdateConfirm.html', table_name=TABLE_NAME, borrow=item, list_user=list_user, list_book=list_book,
                           )

    return render_template('borrow/update.html', table_name=TABLE_NAME, id_name="Borrow ID")


@blueprint.route('/update_confirm', methods=['POST'])
def update_confirm():
    item = Borrow(*request.form.values())
    print(item.username)
    print(item.book_id)
    print(item.borrow_id)
    print(item.secret_key)
    print(item.borrow_date)
    print(item.return_date)

    tgl_pinjam = datetime.fromisoformat(item.borrow_date)
    tgl_kembali = datetime.fromisoformat(item.return_date)

    if tgl_kembali < tgl_pinjam:
        id = request.form['borrow_id']
        item = BorrowController.getByID(id)

        list_user = UserController.getAll()
        list_book = BookController.getAll()

        return render_template('borrow/updateConfirm.html', message='Masukkan tanggal yang benar!', borrow= item,table_name=TABLE_NAME,
                               list_user=list_user, list_book=list_book, secret_key=secret_key)

    BorrowController.update(item)
    return redirect(url_for(TABLE_NAME + '.view'))


@blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        id = request.form['item_id']
        item = BorrowController.getByID(id)

        if item is None:
            return render_template('borrow/delete.html', table_name=TABLE_NAME, id_name="Borrow ID",
                                   message=(TABLE_NAME + " not found"))

        BorrowController.delete(id)

        return redirect(url_for(TABLE_NAME + '.view'))

    return render_template('borrow/delete.html', table_name=TABLE_NAME, id_name="Borrow ID")
