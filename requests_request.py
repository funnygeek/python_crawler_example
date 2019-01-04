import requests
kv= {"key1":"value1","key2":"value2","key3":"value3"}
r = requests.request("GET","http://httpbin.org/post", params = kv)
print(r.url)	# 将kv作为参数加入URL中