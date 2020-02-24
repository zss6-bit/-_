from urllib import request
from urllib import parse
params = {'name':'张三',"age":18,'greet':'hello world'}
qs = parse.urlencode(params)
print(qs)
result = parse.parse_qs(qs)
print(result)