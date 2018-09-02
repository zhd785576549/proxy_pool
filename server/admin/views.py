from flask import render_template
from flask import request


def index():
    return render_template("index.html")


def login():
    if request.method == "GET":
        return render_template("login.html")

