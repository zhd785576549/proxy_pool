from flask import render_template
from flask_login.utils import login_required
from flask import request
from server.admin.forms import AdminLoginForm
from db.exception import UsernameNotExist
from db.interface import get_user_by_username
from werkzeug.security import check_password_hash
from flask import url_for
from flask import redirect
from flask_login import login_user


@login_required
def index():
    return render_template("index.html")


def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        f = AdminLoginForm(request.form)
        if f.validate():
            username = f.username.data
            password = f.password.data
            try:
                user = get_user_by_username(username=username)
                has_password = user.password
                if check_password_hash(pwhash=has_password, password=password):
                    login_user(user)
                    return redirect(url_for("admin.index"))
                else:
                    return render_template("login.html", form=f)
            except UsernameNotExist as e:
                return render_template("login.html", form=f)
        else:
            return render_template("login.html", form=f)

