from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from .crawl import crawler

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'toto'}  # fake user
    posts = crawler.a
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
@app.route('/list')
def list():
    serie = crawler()
    return render_template("list.html")
