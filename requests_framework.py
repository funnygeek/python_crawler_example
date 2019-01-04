import requests

def getHTMLText(url):
	try:
		r = requests.get(url, timeout =30) #timeout可为元组：timeout=(3.05, 27) ，作为connect和read分别的
		r.raise_for_status() #返回值不为200时抛出异常
		r.encoding = r.apparent_encoding 
		#encoding 为从服务器返回的响应头中 Content-Type 获取的字符集编码，若未设置则使用默认的 ISO-8859-1
		#apparent_encoding通过调用chardet.detect()来识别文本编码
		return r.text
	except:
		return "产生异常"

if __name__ =="__main__":
	url = "https://www.baidu.com"
	print(getHTMLText(url))