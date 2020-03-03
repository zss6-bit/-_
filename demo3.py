#urlencode函数的用法：
from urllib import request
from urllib import parse
#params = {'name':'张三',"age":18,'greet':'hello world'}
#result = parse.urlencode(params)
#print(result)
url = 'http://www.baidu.com/s'

params = {"wd":"刘德华"}
qs = parse.urlencode(params)
url = url + "?" +qs
resp = request.urlopen(url)
print(resp.read())