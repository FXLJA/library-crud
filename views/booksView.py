from flask import url_for
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from controllers.bookController import BookController


blueprint = Blueprint("books", __name__, url_prefix="/books")
bc = BookController()


@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_id = request.form['book_id']
        title = request.form['title']
        author = request.form['author']
        book_category = request.form['book_category']

        if bc.getByID(book_id) is not None:
            return render_template('views/addBooks.html', message='ID already exists!')

        b = Book(book_id, title, author, book_category)
        bc.insert(b)

        return redirect(url_for('index'))
    else:
        return render_template('views/addBooks.html')


@blueprint.route('/view')
def view():
    return render_template('/')


@blueprint.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        book_id = request.form['book_id']
        b = bc.getByID(book_id)

        if b is None:
            return render_template('views/updateBooks.html', message="Book not found")

        return render_template('views/UpdateConfirm.html', book=b)
    return render_template('views/updateBooks.html')


@blueprint.route('/update_confirm', methods=['POST'])
def update_confirm():
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']
    book_category = request.form['book_category']

    b = Book(book_id, title, author, book_category)
    bc.update(b)

    return redirect(url_for('index'))


@blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        book_id = request.form['book_id']
        b = bc.getByID(book_id)

        if b is None:
            return render_template('views/deleteBooks.html', message="Book not found")

        bc.delete(b.book_id)
        return redirect(url_for('index'))
    return render_template('views/deleteBooks.html')
