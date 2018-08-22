# coding:utf-8
import requests
import urllib

headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate',
               'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
               'Connection':'Keep-Alive',
                'Cookie':'JSESSIONID=15D7E7EECE928A1CD64FA5505F10A9FC; aliyungf_tc=AQAAALjzzBpXmQMAjdxdZfmXAvKDo1X0; acw_tc=AQAAAEtDeGQfsAMAjdxdZW7gLSa3zPtz; __utma=65168252.1819711876.1519906480.1519906480.1519906480.1; __utmc=65168252; __utmz=65168252.1519906480.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=65168252.5.10.1519906480',
               'Host':'www.chsi.com.cn',
                'Upgrade-Insecure-Requests':'1',
               'Referer':'http://www.chsi.com.cn/cet/',
               'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
def getScore(id):
    encode_name = urllib.quote("林宇航")
    url = "http://www.chsi.com.cn/cet/query?zkzh="+id+"&xm="+encode_name
    response = requests.get(url,headers=headers)

    if not response.content.__contains__('error alignC marginT20'):
        print response.content
        exit(0)


index = 1
for kaochang in range(1,100):
    for zuowei in range(1, 31):
        zuowei=str(zuowei)
        kaochang=str(kaochang)
        if len(zuowei)<=1:
            zuowei="0"+zuowei
        if len(kaochang) < 3:
            kaochang = "0" + kaochang
        if len(kaochang) <= 1:
            kaochang = "00" + kaochang
        
        id="3530101812"+str(kaochang)+str(zuowei)
        print index, " id=" + id
        index = index + 1
        getScore(id)
