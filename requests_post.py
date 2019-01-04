import requests
payload= {"key1":"value1","key2":"value2","key3":"value3"}
r = requests.post("http://httpbin.org/post", data = payload)
print(r.text)	# 键值对储存在form下

r = requests.post("http://httpbin.org/post", data = "QWE")
print(r.text)	# 字符串储存在data下