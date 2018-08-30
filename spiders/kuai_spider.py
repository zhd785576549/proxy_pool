from base import BaseSpider
from tools.agents import agents_list
import requests
import random
import time
from db.interface import insert_proxy_http


class KuaiSpider(BaseSpider):

    def start(self):
        r = requests.get(url="https://www.kuaidaili.com/free", headers=self.get_headers())
        selector = self.get_selector(r.text)
        final_page_num = selector.xpath("//div[@id='listnav']/ul/li/a")[-1].text
        page_range = range(1, int(final_page_num) + 1)
        for page_num in page_range:
            session = requests.Session()
            time.sleep(3)
            page_url = "https://www.kuaidaili.com/free/inha/{0}/".format(page_num)
            r = session.get(url=page_url, headers=self.get_headers())
            response = self.get_selector(r.text)
            self.parse_proxies(response)
            session.close()

    def parse_proxies(self, response):
        trs = response.xpath("//div[@id='list']/table/tbody/tr")[1:]
        for tr in trs:
            ip = tr.xpath("td")[0].text
            port = tr.xpath("td")[1].text
            anonymity = tr.xpath("td")[2].text
            p_type = tr.xpath("td")[3].text
            locate = tr.xpath("td")[4].text
            speed = tr.xpath("td")[5].text
            verify_time = tr.xpath("td")[6].text
            insert_proxy_http(ip=ip, port=port, anonymity=anonymity, p_type=p_type, locate=locate, verify_time=verify_time)

    def get_headers(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'http://www.kuaidaili.com/free',
            'Content-Type': 'text/html;charset=UTF-8',
            'Cache-Control': 'no-cache',
            'Host': 'www.kuaidaili.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random.choice(agents_list)
        }
        return headers


