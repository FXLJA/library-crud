import string
import random

from flask import request
from flask import url_for
from flask import session
from flask import redirect
from flask import Blueprint
from flask import render_template

from Models.borrow import Borrow
from Controllers.book_controller import BookController
from Controllers.user_controller import UserController
from Controllers.borrow_controller import BorrowController

# Insialisasi Blueprint dengan url_prefix borrow
blueprint = Blueprint("borrow", __name__, url_prefix="/admin/borrow")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("admin/borrow/view.html", list_borrow=BorrowController.get_all(), list_book=BookController.get_all(), list_user=UserController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("admin/borrow/insert.html", list_book=BookController.get_all(), list_user=UserController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    book_id = request.form['book_id']
    username = request.form['username']
    secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    borrow_date = request.form['borrow_date']
    return_date = request.form['return_date']

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    borrow = Borrow(None, book_id, username, secret_key, borrow_date, return_date)
    BorrowController.insert(borrow)

    # Redirect ke halaman view
    return redirect(url_for('borrow.view'))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("admin/borrow/update.html", borrow=BorrowController.get_by_id(id), list_book=BookController.get_all(), list_user=UserController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    borrow_id = BorrowController.get_by_id(id).borrow_id
    book_id = request.form['book_id']
    username = request.form['username']
    secret_key = request.form['secret_key']
    borrow_date = request.form['borrow_date']
    return_date = request.form['return_date']

    # Update data tersebut ke dalam database melalui model
    borrow = Borrow(borrow_id, book_id, username, secret_key, borrow_date, return_date)
    BorrowController.update(borrow)

    # Redirect kembali ke view
    return redirect(url_for('borrow.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))

    # Hapus data tersebut dari database
    BorrowController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('borrow.view'))
