import time
import requests
def getHTMLText(url):
	try:
		r = requests.get(url, timeout =30)
		r.raise_for_status() #返回值不为200时抛出异常
		r.encoding = r.apparent_encoding #encoding 为
		return r.text
	except:
		return "1"

if __name__ =="__main__":
	print("begin")
	url = "https://www.baidu.com"
	start_time = time.time()
	for i in range(100):
		a = getHTMLText(url)
		if(a=="1"):
			print("爬取失败")
	end_time = time.time()
	print("爬取100次网页一共消耗:{}秒".format(end_time-start_time))