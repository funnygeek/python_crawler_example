#抓取网页100次，测试性能
import time
import requests
 
def getHtmlText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
 
if __name__ == '__main__':
    url = 'https://www.163.com'
    n = 100
    starts = time.perf_counter()
    for i in range(1,n+1):
        start = time.perf_counter()
        getHtmlText(url)
        diff = time.perf_counter() - start
        print('成功爬取第{}次网页:"{}"需要时间是{:.2f}'.format(i,url,diff))
         
    diffs = time.perf_counter() - starts
    print("成功爬取{}次网页:'{}'总时间为{:.2f}".format(n,url,diffs))
#成功爬取100次网页:'https://www.163.com'总时间为544.43