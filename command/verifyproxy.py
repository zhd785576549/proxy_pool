from base import BaseCommand
from db.interface import fetch_all_enabled_verify_project
from db.interface import fetch_all_http_proxy
from db.interface import insert_http_proxy_quality
import json
import requests
from tools.agents import agents_list
import random


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
            if proxy_type == 0:     # http
                http_proxy_list = fetch_all_http_proxy()
            elif proxy_type == 1:       # https
                http_proxy_list = fetch_all_http_proxy()
            else:
                continue
            for http_proxy in http_proxy_list:
                session = requests.Session()
                try:
                    headers = json.loads(headers)
                    proxies = None
                    if proxy_type == 0:
                        proxies = {
                            "http": "http://{0}:{1}".format(http_proxy.ip, http_proxy.port)
                        }
                    elif proxy_type == 1:
                        proxies = {
                            "https": "https://{0}:{1}".format(http_proxy.ip, http_proxy.port)
                        }
                    headers["User-Agent"] = random.choice(agents_list)
                    if timeout == 0:
                        r = session.get(url=target, headers=headers, proxies=proxies)
                    else:
                        r = session.get(url=target, headers=headers, proxies=proxies, timeout=int(timeout))
                    speed = r.elapsed.total_seconds()
                    insert_http_proxy_quality(verify_project_obj=verify_project, http_proxy_obj=http_proxy, speed=speed)
                except Exception as e:
                    print(e)
                finally:
                    session.close()
