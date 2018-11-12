from . import index_blue
from flask import render_template, flash, redirect, url_for

from app.forms import LoginForm


@index_blue.route('/')
@index_blue.route('/index')
def index():
    user = {'username':"守望者"}
    posts = [
        {
            'author':{'username':'王小波'},
            'body':'我爱破鞋！'
        },
        {
            'author':{'username':'Susan'},
            'body':'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title ='首页', user = user, posts = posts)

@index_blue.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # flash('Login request for OpenId="') + form.openid.data + '", remember_me=' + str(form.remember_me.data)
        flash('你好！ {}'.format( form.username.data ))
        return redirect(url_for('index'))
    return render_template('login.html', title='登录', form = form)
