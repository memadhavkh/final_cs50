from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user , login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
# hash func basically return a hash value for the function that gives a unique value for the given input(password)
# modern-day encryption beleives that given the hash value, the password cannot be retrieved

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged In!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password Incorrect!', category='error')

    return render_template("login.html", user=current_user)

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is already in use', category='error')
        elif username_exists:
            flash('Username is already in use', category='error')
        elif password1 != password2:
            flash('Passwords Don\'t Match', category='error') # esacpe char to include " ' "
        elif len(username) < 2:
            flash("Username too short!", category='error')
        elif len(password1) < 6:
            flash('Password too short!', category='error')
        elif len(email) < 6:
            flash('Email Invalid!', category='error')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password1, method='sha256')) # methdo to hash the pwd
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User Created')
            return redirect(url_for('views.home'))

    return render_template("register.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged Out! Please Log In to access your blogs", category='success')
    return redirect(url_for("auth.login"))



