from base import BaseCommand
from db.interface import fetch_all_enabled_verify_project
from db.interface import fetch_all_http_proxy
from db.interface import insert_http_proxy_quality
import json
import requests
from tools.agents import agents_list
import random
import traceback
import hashlib


class Command(BaseCommand):
    help = "run cron schedule"

    def get_version(self):
        return "v1.0.0"

    def add_parser(self, parser):
        return parser

    def handle(self, *args, **options):
        verify_project_list = fetch_all_enabled_verify_project()
        for verify_project in verify_project_list:
            target = verify_project.target
            timeout = verify_project.timeout
            headers = verify_project.headers
            proxy_type = verify_project.proxy_type
            headers_dict = json.loads(headers)
            if proxy_type == 0:     # http
                http_proxy_list = fetch_all_http_proxy()
            elif proxy_type == 1:       # https
                http_proxy_list = fetch_all_http_proxy()
            else:
                continue
            for http_proxy in http_proxy_list:
                session = requests.Session()
                try:
                    proxies = None
                    if proxy_type == 0:
                        proxies = {
                            "http": "http://{0}:{1}".format(http_proxy.ip, http_proxy.port)
                        }
                    elif proxy_type == 1:
                        proxies = {
                            "https": "https://{0}:{1}".format(http_proxy.ip, http_proxy.port)
                        }
                        headers_dict["User-Agent"] = random.choice(agents_list)
                    if timeout == 0:
                        r = session.get(url=target, headers=headers_dict, proxies=proxies)
                    else:
                        r = session.get(url=target, headers=headers_dict, proxies=proxies, timeout=int(timeout))
                    speed = r.elapsed.total_seconds()
                    key = "sn:{0}:ip:{1}".format(verify_project.sn, http_proxy.ip)
                    unique_key = hashlib.md5(key.encode('utf-8')).hexdigest()
                    # print(unique_key)
                    # print(http_proxy.ip)
                    # print(verify_project.name)
                    insert_http_proxy_quality(verify_project_obj=verify_project, http_proxy_obj=http_proxy,
                                              speed=speed, unique_key=unique_key)
                except Exception as e:
                    # print(e)
                    # traceback.print_exc()
                    pass
                finally:
                    session.close()
