from flask import url_for
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from controllers.bookController import BookController
from models.book import Book
from controllers.categoryController import CategoryController


blueprint = Blueprint("books", __name__, url_prefix="/books")


@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    list_category = CategoryController.getAll()
    if request.method == 'POST':
        b = Book(*request.form.values())

        if BookController.getByID(b.book_id) is not None:
            return render_template('book/addBooks.html', message='ID already exists!', list_category=list_category)

        BookController.insert(b)

        return redirect(url_for('index'))
    else:
        return render_template('book/addBooks.html', list_category=list_category)


@blueprint.route('/view')
def view():
    return render_template('/')


@blueprint.route('/update', methods=['GET', 'POST'])
def update():
    list_category = CategoryController.getAll()
    if request.method == "POST":
        book_id = request.form['book_id']
        b = BookController.getByID(book_id)

        if b is None:
            return render_template('book/updateBooks.html', message="Book not found")

        return render_template('book/UpdateConfirm.html', book=b, list_category=list_category)
    return render_template('book/updateBooks.html')


@blueprint.route('/update_confirm', methods=['POST'])
def update_confirm():
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']
    book_category = request.form['book_category']

    b = Book(book_id, title, author, book_category)
    BookController.update(b)

    return redirect(url_for('index'))


@blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        book_id = request.form['book_id']
        b = BookController.getByID(book_id)

        if b is None:
            return render_template('book/deleteBooks.html', message="Book not found")

        BookController.delete(b.book_id)
        return redirect(url_for('index'))
    return render_template('book/deleteBooks.html')
