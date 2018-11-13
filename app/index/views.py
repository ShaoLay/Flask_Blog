from flask import render_template, flash, redirect, url_for,session,request,g
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db, openid, login
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'username': '守望者'}
    posts = [
        {
            'author': {'username': '王小波'},
            'body': '我爱破鞋'
        },
        {
            'author': {'username': '王小波'},
            'body': '沉默的大多数'
        }
    ]
    return render_template('index.html', title='首页', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('登录失败：用户名或密码不正确！')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='登录', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你，已经成功注册新用户')
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)

# 用户退出登录
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/favicon.ico',methods=['GET'])
def favicon():
    """title左侧图标"""
    return app.send_static_file('favicon.ico')

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username)
    posts = [
        {'author':user, 'body':'Test post #1'},
        {'author':user, 'body':'Test post #2'}
    ]
    return render_template('user.html',user=user, posts=posts)
