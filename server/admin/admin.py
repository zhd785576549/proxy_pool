from flask_admin.contrib.mongoengine import ModelView


class UserAdmin(ModelView):
    column_list = ("username", "is_staff", "is_superuser")


class HttpProxyAdmin(ModelView):
    column_list = ("ip", "port", "locate", "create_at", "update_at")


class VerifyProjectAdmin(ModelView):
    column_list = ("name", "target", "timeout", "headers", "proxy_type",
                   "bo_enable", "brief", "create_at", "update_at")


class HttpProxyQualityAdmin(ModelView):
    column_list = ("verify_project", "speed", "http_proxy", "create_at", "update_at")
    column_filters = ("verify_project",)
    column_editable_list = ()
