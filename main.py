from flask import Flask
from flask import url_for
from flask import session
from flask import request
from flask import redirect
from flask import render_template
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

import constants
from views import booksView
from views import usersView
from models.user import User
from dbController import DBController
from controllers.bookController import BookController
from controllers.userController import UserController

app = Flask(__name__)
app.secret_key = constants.SECRET_KEY

app.config['MYSQL_DATABASE_USER'] = constants.DB_USERNAME
app.config['MYSQL_DATABASE_PASSWORD'] = constants.DB_PASSWORD
app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_DB'] = constants.DB_NAME

db = DBController
db.mysql.init_app(app)

app.register_blueprint(booksView.blueprint)
app.register_blueprint(usersView.blueprint)


@app.route('/')
@app.route('/index')
def index():
    bc = BookController()

    return render_template('index.html', books=bc.getAll(), user_login=('curr_user' in session))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nim = request.form['nim']
        name = request.form['name']
        password = request.form['password']
        gender = request.form['gender']
        uc = UserController()

        if uc.getByID(nim) is not None:
            return render_template('register.html', message='ID already exists!')
        u = User(nim, name, gender, generate_password_hash(password))
        uc.insert(u)
        session['curr_user'] = u.user_name
        return redirect(url_for('index'))
    else:
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nim = request.form['nim']
        password = request.form['password']
        uc = UserController()

        u = uc.getByID(nim)
        if u is None or check_password_hash(u.password, password) is False:
            return render_template('login.html', message='Invalid credentials!')
        session['curr_user'] = u.user_name
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
