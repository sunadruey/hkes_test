import urllib.request
response = urllib.request.urlopen('http://www.baidu.com',timeout=1)
print(response.read())