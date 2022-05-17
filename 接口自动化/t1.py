from django.http.response import JsonResponse
from django.http.response import HttpResponse

# def test(request):
#     if request.mothod=='GET':
#         print('没有对数据库进行改造')
#         return HttpResponse(content='test',status=200)
#     if request.mothod == 'POST':
#         print('对数据库进行改造')
#         return JsonResponse(headers={"test":123},data={"data":123}, status=200)


from requests import request

# req = request(method="post", url="http://127.0.0.1:8080/login", data={"password": "123456", "username": "123456"})
# print(req.content)



a=1
b=2
assert a>b ,'cuowu '
print('zq')
