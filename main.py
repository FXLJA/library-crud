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

from Views.UserViews import user_book_view
from Views.UserViews import user_borrow_view

from Controllers.book_controller import BookController
from Controllers.user_controller import UserController
from Controllers.admin_controller import AdminController
from Controllers.borrow_controller import BorrowController

from Views.AdminViews import user_view
from Views.AdminViews import book_view
from Views.AdminViews import admin_view
from Views.AdminViews import borrow_view
from Views.AdminViews import category_view

app = Flask(__name__)
app.secret_key = constants.SECRET_KEY

app.config['MYSQL_DATABASE_USER'] = constants.DB_USERNAME
app.config['MYSQL_DATABASE_PASSWORD'] = constants.DB_PASSWORD
app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_DB'] = constants.DB_NAME

MyDatabase.mysql.init_app(app)

# Admin blueprint
app.register_blueprint(book_view.blueprint)
app.register_blueprint(user_view.blueprint)
app.register_blueprint(borrow_view.blueprint)
app.register_blueprint(category_view.blueprint)
app.register_blueprint(admin_view.blueprint)

# User blueprint
app.register_blueprint(user_book_view.blueprint)
app.register_blueprint(user_borrow_view.blueprint)


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        password = request.form['password']
        gender = request.form['gender']
        uc = UserController()

        if uc.get_by_id(username) is not None:
            return render_template('auth/sign-up.html', message='ID already exists!')
        u = User(username, name, generate_password_hash(password), gender)
        uc.insert(u)
        session['curr_user'] = u.name
        return redirect(url_for('index'))
    else:
        return render_template('auth/sign-up.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        uc = UserController()

        u = uc.get_by_id(username)
        a = AdminController.get_by_id(username)

        if u is not None and check_password_hash(u.password, password):
            session.clear()
            session['curr_user'] = u.username
            return redirect(url_for('user_book.view'))
        elif a is not None and password == a.password:
            session.clear()
            session['admin'] = a.username
            return redirect(url_for('user.view'))
        else:
            return render_template('auth/sign-in.html', message='Invalid credentials!')
    else:
        return render_template('auth/sign-in.html')


@app.route('/auth/sign-out/')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    constants.APP = app
    app.run(debug=True)
