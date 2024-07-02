from flask import Blueprint,session, render_template, redirect, url_for, request
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from forms.forget_password_form import ResetForm
from models.user import Users
from config import db
from werkzeug.security import generate_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if not ('login' in session):
        if request.method == 'POST':
            if form.validate_on_submit():
                user = Users.query.filter_by(email = request.form['email']).first()
                session['login'] = user.id
                return redirect(url_for('home.index'))
            else:
                return render_template("auth/login.html", title = "Login", form = form)
        else:
            return render_template("auth/login.html", title = "Login", form = form)
    else:
        return redirect(url_for('home.index'))
    

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if not ('login' in session):
        if request.method == 'POST':
            if form.validate_on_submit():
                name = request.form['name']
                email = request.form['email']
                password = generate_password_hash(request.form['password'])
                user = Users(name = name, email = email, password = password)
                db.session.add(user)
                db.session.commit()
                session['login'] = user.id
                return redirect(url_for('home.index'))
            else:
                return render_template("auth/register.html", title = "Register", form = form)
        else:
            return render_template("auth/register.html", title = "Register", form = form)
    else:
        return redirect(url_for('home.index'))
    

@auth.route('/reset', methods = ['GET', 'POST'])
def reset():
    form = ResetForm()
    if not ('login' in session):
        if request.method == 'POST':
            if form.validate_on_submit():
                user = Users.query.filter_by(email = request.form['email']).first()
                user.password = generate_password_hash(request.form['password'])
                db.session.commit()
                return redirect(url_for('auth.login'))
            else:
                return render_template("auth/forget_password.html", title = "Forget Password", form = form)
        return render_template("auth/forget_password.html", title = "Forget Password", form = form)
    else:
        return redirect(url_for('home.index'))
    
@auth.route('/logout', methods = ['GET', 'POST'])
def logout():
    if request.method == 'POST' or request.method == 'GET':
        if 'login' in session:
            session.pop('login')
        return redirect(url_for('home.index'))