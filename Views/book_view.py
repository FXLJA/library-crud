from flask import Blueprint, render_template, request, redirect, url_for, session
from Controllers.book_controller import BookController
from Models.book import Book
from Controllers.category_controller import CategoryController

# Insialisasi Blueprint dengan url_prefix book
blueprint = Blueprint("book", __name__, url_prefix="/admin/book")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("admin/book/view.html", list_book=BookController.get_all(),
                           list_category=CategoryController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("admin/book/insert.html", list_category=CategoryController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']
    thumbnail = request.form['thumbnail']
    file_path = request.form['file_path']
    category_id = request.form['category_id']

    # Cek apakah book_id sudah ada dalam database
    if BookController.get_by_id(book_id) is not None:
        # jika iya, tampilkan error message
        return render_template('admin/book/insert.html', message="book_id sudah pernah terdaftar!",
                               list_category=CategoryController.get_all())

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    book = Book(book_id, title, author, thumbnail, file_path, category_id)
    BookController.insert(book)

    # Redirect ke halaman view
    return redirect(url_for('book.view'))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("admin/book/update.html", book=BookController.get_by_id(id),
                               list_category=CategoryController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    book_id = BookController.get_by_id(id).book_id
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
@blueprint.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))

    # Hapus data tersebut dari database
    BookController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('book.view'))
