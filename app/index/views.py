from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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


# @app.route('/login', methods=['GET', 'POST'])
@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('正在登录的用户是：   {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='登录', form=form)


@app.route('/favicon.ico',methods=['GET'])
def favicon():
    """title左侧图标"""
    return app.send_static_file('favicon.ico')