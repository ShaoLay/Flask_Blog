# from flask import render_template
# from flask_login import login_required
#
# from app import app
# from app.models import User
#
#
# @app.route('/user/<username>')
# @login_required
# def user(username):
#     user = User.query.filter_by(username=username)
#     posts = [
#         {'author':user, 'body':'Test post #1'},
#         {'author':user, 'body':'Test post #2'}
#     ]
#     return render_template('user.html',user=user, posts=posts)