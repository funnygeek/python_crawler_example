import requests
r = requests.get("http://www.baidu.com", timeout =30)
print(r.headers)
print(r.text)
r = requests.head("http://www.baidu.com", timeout =30)
print(r.headers)
print(r.text)
# 需要获取headers时，head方法只会获取Headers，不会读取text，相比于get方法能大大减少网络带宽消耗，提升性能