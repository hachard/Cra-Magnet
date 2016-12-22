from flask import render_template, flash, redirect
from app import app
import requests
import re
from .crawl import crawler

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    user = {'nickname': 'toto'}  # fake user
    posts = crawler.tv_show()
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
