from flask import render_template
from flask_login.utils import login_required
from flask import request
from server.admin.forms import AdminLoginForm


@login_required
def index():
    return render_template("index.html")


def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        f = AdminLoginForm(request.form)
        print(f.validate())
        if f.validate():
            pass
        else:
            return render_template("login.html", form=f)

