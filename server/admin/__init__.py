from flask import Flask
from flask_login import LoginManager
from flask_session import Session
from server.admin import views
from server.admin import settings
from flask_admin import Admin
from flask_mongoengine import MongoEngine
from server.admin import admin as server_admin
from db import tables
from conf import settings


app = Flask(__name__)

app.config.from_object('server.admin.settings')

# initialize login
login_manager = LoginManager()
login_manager.login_view = "/login"
login_manager.init_app(app)
Session(app)

# mongodb engine
db = MongoEngine()
app.config['MONGODB_SETTINGS'] = {
    'db': settings.DATABASE["NAME"],
    'host': settings.DATABASE["HOST"],
    'port': settings.DATABASE["PORT"]
}
db.init_app(app)


@login_manager.user_loader
def get_user(user_id):
    print(user_id)
    return None


app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/login", view_func=views.login, methods=["GET", "POST"])


def start_api_server(host, port):
    # Create admin

    admin = Admin(app, name="管理系统")

    # Add views
    admin.add_view(server_admin.UserAdmin(tables.User))
    admin.add_view(server_admin.HttpProxyAdmin(tables.HttpProxy))
    admin.add_view(server_admin.VerifyProjectAdmin(tables.VerifyProject))
    admin.add_view(server_admin.HttpProxyQualityAdmin(tables.HttpProxyQuality))

    app.run(host=host, port=port)
