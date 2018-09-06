from base import BaseSpider
from tools.agents import agents_list
import requests
import random
import time
from db.interface import insert_proxy_http
from tools.proxy import get_proxies


class Spider(BaseSpider):

    def start(self):
        r = requests.get(url="http://www.xicidaili.com/wt/", headers=self.get_headers())
        selector = self.get_selector(r.text)
        final_page_num = selector.xpath("//div[@class='pagination']/a")[-2].text
        page_range = range(1, int(final_page_num) + 1)
        for page_num in page_range:
            session = requests.Session()
            time.sleep(3)
            page_url = "http://www.xicidaili.com/wt/{0}".format(page_num)
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
        print(response)
        trs = response.xpath("//table[@id='ip_list']/tr")[1:]
        for tr in trs:
            ip = tr.xpath("td")[1].text
            port = tr.xpath("td")[2].text
            locate = tr.xpath("td")[3].xpath("a")[0].text
            insert_proxy_http(ip=ip, port=port, locate=locate)

    def get_headers(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www.xicidaili.com/wt/',
            'Content-Type': 'text/html;charset=UTF-8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'www.xicidaili.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random.choice(agents_list)
        }
        return headers


