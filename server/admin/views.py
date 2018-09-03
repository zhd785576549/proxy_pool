from flask import render_template
from flask_login.utils import login_required
from flask import request


@login_required
def index():
    return render_template("index.html")


def login():
    if request.method == "GET":
        return render_template("login.html")

