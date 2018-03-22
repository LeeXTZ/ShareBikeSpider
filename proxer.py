# coding:utf-8

import requests
from bs4 import BeautifulSoup


class SpiderProxy(object):
    headers = {
        "Host": "www.xicidaili.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://www.xicidaili.com/wt/1",
    }

    def __init__(self, session_url):
        self.req = requests.session()
        self.req.get(session_url)

    def get_pagesource(self, url):
        html = self.req.get(url, headers=self.headers)
        return html.content

    def get_all_proxy(self, url, n):
        data = []
        for i in range(1, n):
            html = self.get_pagesource(url + str(i))
            soup = BeautifulSoup(html, "lxml")

            table = soup.find('table', style='margin: 20px;')
            for row in table.findAll("tr"):
                cells = row.findAll("td")
                tmp = []
                for item in cells:
                    tmp.append(item.find(text=True))
                data.append(tmp[1:3])
        return data

session_url = 'http://www.xicidaili.com/wt/1'
#session_url = 'http://www.cybersyndrome.net/plr6.html'
url = 'http://www.xicidaili.com/wt/'
# url = 'http://www.cybersyndrome.net/plr6.html'
p = SpiderProxy(session_url)
proxy_ip = p.get_all_proxy(url, 5)

proxy_list = []
good_proxy = []
n = 0


for i in range(0, 100):
    if proxy_ip[i]:
        n += 1
        proxy = 'http://' + proxy_ip[i][0] + ':' + proxy_ip[i][1]
        proxy_list.append(proxy)
        print(proxy)

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

for i in range(0, 100):
    try:
        proxies = dict(http=proxy_list[i])
        r = requests.get("http://www.dancheditu.com:3000/bikes?lat=30.462675&lng=114.164457&cityid=218", timeout=2, proxies=proxies)
        r.raise_for_status()
        good_proxy.append(proxies)
        print('可用')
        print('已找到' + str(len(good_proxy)) + '个可用')
    except Exception:
        print('不可用')
        continue

print(len(good_proxy))
print(good_proxy)


with open('proxy.txt', 'a') as f:
    f.write('\n'+str(good_proxy))
