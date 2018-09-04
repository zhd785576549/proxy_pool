from flask_admin.contrib.mongoengine import ModelView
from flask_admin import AdminIndexView
from flask_admin import expose
from flask_login import current_user
from flask_login.login_manager import user_accessed
from flask import request
from flask import url_for
from flask import redirect
import uuid


class MyAdminIndexView(AdminIndexView):

    @expose("/")
    def index(self):
        if not current_user.is_authenticated:
            next_url = request.url
            login_url = '%s?next=%s' % (url_for('login'), next_url)
            return redirect(login_url)
        if current_user.is_active is False:
            return user_accessed("user is not active")

        if current_user.is_staff is False:
            return user_accessed("user is not staff")

        if current_user.is_active is True:
            return super(MyAdminIndexView, self).index()
        else:
            return redirect(url_for("main"))


class UserAdmin(ModelView):
    column_list = ("username", "is_staff", "is_superuser")


class HttpProxyAdmin(ModelView):
    column_list = ("ip", "port", "locate", "create_at", "update_at")


class VerifyProjectAdmin(ModelView):
    column_list = ("name", "sn", "target", "timeout", "headers", "proxy_type",
                   "bo_enable", "brief", "create_at", "update_at")

    def on_model_change(self, form, model, is_created):
        if model.sn is None or len(model.sn) == 0:
            model.sn = str(uuid.uuid1())
            model.save()


class HttpProxyQualityAdmin(ModelView):
    column_list = ("verify_project", "speed", "unique_key", "http_proxy", "create_at", "update_at")
    column_filters = ("verify_project",)
    column_editable_list = ()
