from app import app2 as app
from flask import render_template, flash, redirect, url_for
from app.Forms import LoginForm
from app.models import Post, User
from flask_login import current_user, login_user, logout_user

@app.route('/')
@app.route('/Index')
def Index():
        user2 = {'username4': 'moto'}

        a3title = {'username15': 'Dov'}

        posts2 = Post.query.all()



        return render_template('Index.html', user1=user2, posts5=posts2, title=a3title)
@app.route('/store')
def store():
        items6 = [
            {
                'title': "Python book",
                'price': "200"
            },
            {
                'title': "Cook book",
                'price': 2
            },
            {
                'title': "iphone X",
                'price': 1000
            }
        ]
        return render_template('store.html', items5=items6)

@app.route('/Login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Index'))
    form = LoginForm()
    if form.validate_on_submit():# post and submit validate

        # get the user from data base use code
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('Login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('Index'))

    return render_template('Login.html', title='Sign In', form=form) # GET or submit validate Flaid

@app.route('/logout')
def logout():
        logout_user()
        return redirect(url_for('Index'))