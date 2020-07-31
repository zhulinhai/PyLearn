#ip地址归属地查询
import requests

url = 'https://site.ip138.com/'

try:
    r = requests.get(url + 'www.baidu.com')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
