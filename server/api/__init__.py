from flask import Flask
from server.api import views

app = Flask(__name__)

app.add_url_rule("/test", view_func=views.fetch)


def start_api_server(host, port):
    app.run(host=host, port=port)
