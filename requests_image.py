import requests
path ="D:/test/abc.jpg"
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
r = requests.get(url)
print(r.status_code)
#读取目标图片并将其存储至本地路径
#标准的Python文件操作需要try open finally close 等一系列操作，所以使用with语句来自动调用close()方法
with open(path, 'wb') as f:
	f.write(r.content)