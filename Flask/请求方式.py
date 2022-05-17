from requests import request

# req=request(method='d',url='http://127.0.0.1:5000/hello')
# print(req.text)


json1={'uname':'xxx'}
data1={'pwd':'yyy'}
req=request(method="post",url='http://127.0.0.1:5000/query/',json=json1)
print(req.text)