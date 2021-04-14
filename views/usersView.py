"""
Modul view untuk objek 'users'. Menangani perintah CRUD yang diberikan melalui user interface.
Perintah CRUD akan dicocokkan dengan parameter yang ada pada modul 'models' ketika objek dikonstruksi.

Modul ini juga memiliki penanganan exception handling untuk mencegah eksepsi sebagai berikut:
DuplicateEntryException: eksepsi ketika terdeteksi entry dalam database yang memiliki nilai primary key yang sama
NotFoundException: eksepsi ketika objek dengan primary key tertentu tidak ditemukan
"""

from flask import Blueprint
from flask import render_template

from controllers.usersController import UsersController

blueprint = Blueprint("users", __name__, url_prefix="/users")
uc = UsersController()


@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('views/addUsers.html')


@blueprint.route('/view')
def view():
    return render_template('views/viewUsers.html')
