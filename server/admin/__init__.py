from flask import Flask
from flask_login import LoginManager
from flask_session import Session
from server.admin import views
from server.admin import settings


app = Flask(__name__)

app.config.from_object('server.admin.settings')

# initialize login
login_manager = LoginManager()
login_manager.login_view = "/login"
login_manager.init_app(app)
Session(app)


@login_manager.user_loader
def get_user(user_id):
    print(user_id)
    return None


app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/login", view_func=views.login, methods=["GET", "POST"])


def start_api_server(host, port):
    app.run(host=host, port=port)
