from flask import request
from flask import url_for
from flask import session
from flask import redirect
from flask import Blueprint
from flask import render_template

from Models.admin import Admin
from Controllers.admin_controller import AdminController

# Insialisasi Blueprint dengan url_prefix admin
blueprint = Blueprint("admin", __name__, url_prefix="/admin/admin")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session admin tidak ada, redirect kembali ke index
    if session.get('admin') is None:
        return redirect(url_for('index'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("Views/admin/view.html", list_admin=AdminController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session admin tidak ada, redirect kembali ke index
    if session.get('admin') is None:
        return redirect(url_for('index'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("Views/admin/insert.html")

    # Jika metodenya adalah post, dapatkan data dari post
    username = request.form['username']
    password = request.form['password']

    # Cek apakah username sudah ada dalam database
    if AdminController.get_by_id(username) is not None:
        # jika iya, tampilkan error message
        return render_template('Views/admin/insert.html', message="username sudah pernah terdaftar!")

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    admin = Admin(username, password)
    AdminController.insert(admin)

    # Redirect ke halaman view
    return redirect(url_for('admin.view'))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    # Jika session admin tidak ada, redirect kembali ke index
    if session.get('admin') is None:
        return redirect(url_for('index'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("Views/admin/update.html", admin=AdminController.get_by_id(id))

    # Jika metodenya adalah post, dapatkan data dari post
    username = request.form['username']
    password = request.form['password']

    # Update data tersebut ke dalam database melalui model
    admin = Admin(username, password)
    AdminController.update(admin)

    # Redirect kembali ke view
    return redirect(url_for('admin.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    # Jika session admin tidak ada, redirect kembali ke index
    if session.get('admin') is None:
        return redirect(url_for('index'))

    # Hapus data tersebut dari database
    AdminController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('admin.view'))
