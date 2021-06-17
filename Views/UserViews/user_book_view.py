from flask import request
from flask import url_for
from flask import session
from flask import redirect
from flask import Blueprint
from flask import render_template

from Models.book import Book
from Controllers.book_controller import BookController
from Controllers.category_controller import CategoryController

# Insialisasi Blueprint dengan url_prefix book
blueprint = Blueprint("user_book", __name__, url_prefix="/user/book")


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
