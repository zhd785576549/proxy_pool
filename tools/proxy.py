import random
import requests


def get_proxies():
    proxiy_api_list = [
        "http://10.1.10.10:21101/api/v1/fetch_recent?target=www.ipe.org.cn",
        "http://10.1.10.10:21101/api/v1/fetch_recent?target=qyxy.baic.gov.cn",
        "http://10.1.10.10:21101/api/v1/fetch_recent?target=www.gsxt.gov.cn",
        "http://10.1.10.10:21101/api/v1/fetch_recent?target=www.nacao.org.cn",
        "http://10.1.10.10:21101/api/v1/fetch_recent?target=wenshu.court.gov.cn",
        "http://10.1.10.10:21101/api/v1/fetch_recent?target=www.creditchina.gov.cn",
    ]
    url = random.choice(proxiy_api_list)
    r = requests.get(url)
    proxies_list = r.text.split("\r\n")
    proxies = {'http': 'http://%s' % random.choice(proxies_list)}
    return proxies