from flask import Flask ,request
"""
flask 就是构建一个路由地址
"""

#实例化
app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False # 当data值有中文字符时  提供解码功能

# @app.route('/')  # 完成一个flask的接口构造,地址为： http://127.0.0.1:5000，若/后面无参数可以隐藏
# def hello():
#     return 'hello world'
#
# @app.route('/hello')  # http://127.0.0.1:5000/hello
# def hello2():
#     return '你好'
#
# @app.route('/hello',methods=['d'])  # http://127.0.0.1:5000/hello
# def hello3():
#     return '华测'

# 模拟请求方式

# @app.route('/query/')  # 包含请求参数的请求
# def hello4():
#     print(request.args) # 获取get的请求参数
#     print(request.args.get('data')) # 获取get的请求参数
#     return str(request.args)

@app.route('/query/',methods=['post'])  # 包含请求参数的请求
def hello5():
    print(request.json)
    print(request.json.get('uname')) # 获取post的请求参数
    # print(request.data) # 获取post的请求参数
    return 'aaa'

if __name__ == '__main__':
    app.run()   # 返回的值是 http://127.0.0.1:5000，点开链接，网页显示了“hello ”