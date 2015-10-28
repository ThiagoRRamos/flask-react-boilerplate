from urllib.parse import urlparse

from flask import Blueprint, render_template, request, session, redirect, url_for

from database import db_session
from models.users import User
from views import utils

user = Blueprint('user', __name__)

@user.route('/login', methods=['GET', 'POST'])
def login():
    wrong_password = False
    if request.method == 'POST':
        user = User.query.filter(User.username == request.form['username']).first()
        if user and user.check_password(request.form['password']):
            session['user_id'] = user.id
            next = request.args.get('next')
            if next and urlparse(next).netloc == '':
                return redirect(request.args.get('next'))
            return redirect(url_for('home.index'))
        wrong_password = True
    return render_template('user/login.html', wrong=wrong_password)

@user.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if not User.query.filter(User.username == request.form['username']).first():
            if not User.query.filter(User.email == request.form['email']).first():
                if request.form['password'] == request.form['confirm-password']:
                    user = User(username=request.form['username'], email=request.form['email'], password=request.form['password'])
                    db_session.add(user)
                    db_session.commit()
                    return redirect(url_for('.login'))
    return render_template('user/signup.html')

@user.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home.index'))

@user.route('/profile')
@utils.login_required
def profile():
    return render_template('user/profile.html')