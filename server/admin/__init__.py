from flask import Flask
from server.admin import views

app = Flask(__name__)

app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/login", view_func=views.login, methods=["GET", "POST"])


def start_api_server(host, port):
    app.run(host=host, port=port)
