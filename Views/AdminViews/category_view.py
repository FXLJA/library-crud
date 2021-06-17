from flask import request
from flask import url_for
from flask import session
from flask import redirect
from flask import Blueprint
from flask import render_template

from Models.category import Category
from Controllers.category_controller import CategoryController

# Insialisasi Blueprint dengan url_prefix category
blueprint = Blueprint("category", __name__, url_prefix="/admin/category")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("admin/category/view.html", list_category=CategoryController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("admin/category/insert.html")

    # Jika metodenya adalah post, dapatkan data dari post
    category_id = request.form['category_id']
    category_name = request.form['category_name']

    # Cek apakah category_id sudah ada dalam database
    if CategoryController.get_by_id(category_id) is not None:
        # jika iya, tampilkan error message
        return render_template('admin/category/insert.html', message="category_id sudah pernah terdaftar!")

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    category = Category(category_id, category_name)
    CategoryController.insert(category)

    # Redirect ke halaman view
    return redirect(url_for('category.view'))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("admin/category/update.html", category=CategoryController.get_by_id(id))

    # Jika metodenya adalah post, dapatkan data dari post
    category_id = CategoryController.get_by_id(id).category_id
    category_name = request.form['category_name']

    # Update data tersebut ke dalam database melalui model
    category = Category(category_id, category_name)
    CategoryController.update(category)

    # Redirect kembali ke view
    return redirect(url_for('category.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))

    # Hapus data tersebut dari database
    CategoryController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('category.view'))
