from flask import Flask
from flask import url_for
from flask import session
from flask import request
from flask import redirect
from flask import render_template
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

import constants
from my_database import MyDatabase

from Models.user import User
from Views import book_view
from Views import user_view
from Views import admin_view
from Views import borrow_view
from Views import category_view

from Views.UserViews import user_book_view
from Views.UserViews import user_borrow_view

from Controllers.book_controller import BookController
from Controllers.user_controller import UserController
from Controllers.borrow_controller import BorrowController

app = Flask(__name__)
app.secret_key = constants.SECRET_KEY

app.config['MYSQL_DATABASE_USER'] = constants.DB_USERNAME
app.config['MYSQL_DATABASE_PASSWORD'] = constants.DB_PASSWORD
app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_DB'] = constants.DB_NAME

MyDatabase.mysql.init_app(app)

app.register_blueprint(book_view.blueprint)
app.register_blueprint(user_view.blueprint)
app.register_blueprint(borrow_view.blueprint)
app.register_blueprint(category_view.blueprint)
app.register_blueprint(admin_view.blueprint)

# user blueprint
app.register_blueprint(user_book_view.blueprint)
app.register_blueprint(user_borrow_view.blueprint)


@app.route('/')
@app.route('/index')
def index():
    bc = BookController()
    session['admin'] = 'admin'
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nim = request.form['nim']
        name = request.form['name']
        password = request.form['password']
        gender = request.form['gender']
        uc = UserController()

        if uc.getByID(nim) is not None:
            return render_template('auth/sign-up.html', message='ID already exists!')
        u = User(nim, name, generate_password_hash(password), gender)
        uc.insert(u)
        session['curr_user'] = u.user_name
        return redirect(url_for('index'))
    else:
        return render_template('auth/sign-up.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nim = request.form['nim']
        password = request.form['password']
        uc = UserController()

        u = uc.getByID(nim)
        if u is None or check_password_hash(u.password, password) is False:
            return render_template('auth/sign-in.html', message='Invalid credentials!')
        session['curr_user'] = u.user_name
        return redirect(url_for('user.view'))
    else:
        return render_template('auth/sign-in.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/borrow/add', methods=['GET', 'POST'])
def addBorrow():
    if request.method == 'POST':
        borrow_id = request.form['borrow_id']
        book_name = request.form['book_id']
        user_id = request.form['user_id']
        borrow_date = request.form['borrow_date']
        return_date = request.form['return_date']
        bc = BorrowController()


if __name__ == '__main__':
    app.run(debug=True)
