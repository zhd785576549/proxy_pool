from db.tables import HttpProxy
from db.tables import VerifyProject
from db.tables import HttpProxyQuality
from db.tables import User
from mongoengine import errors
from db import exception


def insert_proxy_http(**kwargs):
    ip = kwargs.pop("ip")
    port = kwargs.pop("port")
    locate = kwargs.pop("locate", None)

    http_proxy = HttpProxy()
    http_proxy.ip = ip
    http_proxy.port = port
    http_proxy.locate = locate

    try:
        http_proxy.save()
    except errors.NotUniqueError as e:
        pass
    except Exception as e:
        print(e)


def fetch_all_http_proxy():
    """
    Fetch all proxy
    :return: [queryset]
        list of http proxy
    """
    http_proxy_list = HttpProxy.objects.all()
    return http_proxy_list


def fetch_all_enabled_verify_project():
    """
    Fetch all enabled verify project
    :return: [queryset]
        list of verify project information
    """
    verify_project_list = VerifyProject.objects(bo_enable=True)
    return verify_project_list


def insert_http_proxy_quality(verify_project_obj, http_proxy_obj, speed):
    http_proxy_quality = HttpProxyQuality()
    http_proxy_quality.http_proxy = http_proxy_obj
    http_proxy_quality.verify_project = verify_project_obj
    http_proxy_quality.speed = speed
    http_proxy_quality.save()


def insert_user(username, password, is_superuser=False, is_staff=False):
    """
    Insert one user
    :param username:
    :param password:
    :param is_superuser:
    :param is_staff:
    :return:
    """
    user = User()
    user.username = username
    user.password = password
    user.is_superuser = is_superuser
    user.is_staff = is_staff
    return user.save()


def get_user_by_username(username):
    """
    Get user by username
    :param username: [str] username
    :return: [User]
        object of User(Document)
    """
    user = User.objects(username=username)
    if len(user):
        return user[0]
    else:
        raise exception.UsernameNotExist


def get_user_by_pk(id):
    user = User.objects(id=id)
    if len(user):
        return user[0]
    else:
        raise exception.UserNotExist
