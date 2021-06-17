import os

from flask import request
from flask import url_for
from flask import session
from flask import redirect
from flask import Blueprint
from flask import render_template
from werkzeug.utils import secure_filename

from Models.book import Book
from Controllers.book_controller import BookController
from Controllers.category_controller import CategoryController

# Insialisasi Blueprint dengan url_prefix book
blueprint = Blueprint("user_book", __name__, url_prefix="/user/book")

THUMBNAIL_EXTENSION = {'png', 'jpg', 'jpeg', 'svg', 'bmp'}
FILE_EXTENSION = {'pdf', 'txt', 'docx'}


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session user tidak ada, redirect kembali ke index
    if session.get('curr_user') is None:
        return redirect(url_for('index'))
    # Jika session user ada, tampilkan halaman view
    return render_template("user/book/view.html", list_book=BookController.get_all(),
                           list_category=CategoryController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session user tidak ada, redirect kembali ke index
    if session.get('admin') is None:
        return redirect(url_for('index'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("user/book/insert.html", list_category=CategoryController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']
    thumbnail = request.form['thumbnail']
    file_buku = request.form['file_path']
    category_id = request.form['category_id']

    # Cek apakah book_id sudah ada dalam database
    if BookController.get_by_id(book_id) is not None:
        # jika iya, tampilkan error message
        return render_template('user/book/insert.html', message="book_id sudah pernah terdaftar!",
                               list_category=CategoryController.get_all())

    if not allowed_file(thumbnail.filename, THUMBNAIL_EXTENSION):
        return render_template('user/book/insert.html', message="Ekstensi thumbnail salah!",
                               list_category=CategoryController.get_all())

    if not allowed_file(file_buku.filename, FILE_EXTENSION):
        return render_template('user/book/insert.html', message="Ekstensi buku salah!",
                               list_category=CategoryController.get_all())

    thumbnail.save(os.path.join('/static/thumbnails', secure_filename(thumbnail.filename)))
    file_buku.save(os.path.join('/static/books', secure_filename(file_buku.filename)))

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    book = Book(book_id, title, author, secure_filename(thumbnail.filename), secure_filename(file_buku.filename),
                category_id)
    BookController.insert(book)

    # Redirect ke halaman view
    return redirect(url_for('book.view'))


def allowed_file(filename, allowed_extension):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extension


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    # Jika session user tidak ada, redirect kembali ke index
    if session.get('admin') is None:
        return redirect(url_for('index'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("user/book/update.html", book=BookController.get_by_id(id),
                               list_category=CategoryController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']
    thumbnail = request.form['thumbnail']
    file_path = request.form['file_path']
    category_id = request.form['category_id']

    # Update data tersebut ke dalam database melalui model
    book = Book(book_id, title, author, thumbnail, file_path, category_id)
    BookController.update(book)

    # Redirect kembali ke view
    return redirect(url_for('book.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    # Jika session user tidak ada, redirect kembali ke index
    if session.get('admin') is None:
        return redirect(url_for('index'))

    # Hapus data tersebut dari database
    BookController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('book.view'))
