from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'toto'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'Joe'},
            'body': 'Lorem ipsum dolor sit amet.'
        },
        {
            'author': {'nickname': 'Sus'},
            'body': 'Excepteur sint occaecat cupidatat non proident!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
@app.route('/list')
def list():
    serie = crawler()
    return render_template("list.html")
