import requests
import multiprocessing
import time
from bs4 import BeautifulSoup

base_url = 'http://www.ip181.com/'
proxy_list = []

def get_181_free_proxies():
    try:
        global proxy_list
        p = requests.get(base_url)
        requests.encoding = "gb2312"
        html = p.text
        soup = BeautifulSoup(html,"html.parser")
        content = soup.find("tbody")
        tr_list = content.find_all("tr")
        for x in range(1,len(tr_list)):
            one_tr = tr_list[x]
            ip = one_tr.find_all("td")[0].text
            port = one_tr.find_all("td")[1].text
            kuai_proxy = 'http://' + ip+":"+port
            proxy_list.append(kuai_proxy)
        return proxy_list
    except Exception as e:
        print (e)

def test_proxies(proxy):
    myproxies = dict(http=proxy)
    try:
        r = requests.get('http://www.dancheditu.com:3000/bikes?lat=30.462675&lng=114.164457&cityid=218',
                         timeout=5, proxies=myproxies)
        r.raise_for_status()
    except Exception as e:
        print(e)
        print('不可用')
    else:
        print('可用')
        print(dict(http=proxy))
        with open('proxy.txt', 'a') as f:
            f.write(str(dict(http=proxy)) + ',\n')
        print('本次写入完成')

if __name__ == '__main__':
    t1 = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    for i in range(100):
        myproxy_list = get_181_free_proxies()
        pool = multiprocessing.Pool(4)
        pool.map(test_proxies, myproxy_list)
        pool.close()
        pool.join()
        #t2 = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        #print('<-<-<-<-<end at:', t2)
        time.sleep(550)
