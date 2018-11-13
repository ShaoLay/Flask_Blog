from flask import render_template, flash, redirect, url_for,session,request,g
from flask_login import current_user, login_user
from werkzeug.urls import url_parse

from app import app, db, openid, login
from app.forms import LoginForm
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



@app.route('/favicon.ico',methods=['GET'])
def favicon():
    """title左侧图标"""
    return app.send_static_file('favicon.ico')