from base import BaseSpider
from tools.agents import agents_list
import requests
import random
import time
from db.interface import insert_proxy_http
from db.interface import insert_proxy_https


class Spider(BaseSpider):

    def start(self):
        r = requests.get(url="http://ip.jiangxianli.com/", headers=self.get_headers())
        selector = self.get_selector(r.text)
        final_page_num = selector.xpath("//div[1]/div/div[1]/ul/li[12]/a")[0].text
        page_range = range(1, int(final_page_num) + 1)
        for page_num in page_range:
            session = requests.Session()
            time.sleep(3)
            page_url = "http://ip.jiangxianli.com/?page={0}".format(page_num)
            try:
                r = session.get(url=page_url, headers=self.get_headers(), timeout=10)
                response = self.get_selector(r.text)
                print("TOTAL PAGES: %s, CUR PAGE: %s" % (final_page_num, page_num))
                self.parse_proxies(response)
            except Exception as e:
                print(e)
            finally:
                session.close()

    def parse_proxies(self, response):
        trs = response.xpath("//div[1]/div/div[1]/div[2]/table/tbody/tr")[1:]
        for tr in trs:
            ip = tr.xpath("td")[1].text
            port = tr.xpath("td")[2].text
            protocol = tr.xpath("td")[4].text
            locate = tr.xpath("td")[5].text
            amous = tr.xpath("td")[3].text
            # print(ip, port, protocol, locate, amous)
            if amous == u"高匿":
                if protocol == "HTTP":
                    insert_proxy_http(ip=ip, port=port, locate=locate)
                elif protocol == "HTTPS":
                    insert_proxy_https(ip=ip, port=port, locate=locate)

    def get_headers(self):
        headers = {
            'Accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'ip.jiangxianli.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random.choice(agents_list)
        }
        return headers


