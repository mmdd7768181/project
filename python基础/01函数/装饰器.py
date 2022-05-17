from   functools import wraps
import logging
'''
一种语法结构
定义一个方法，通过@+方法名的这种方式来简化函数间相互引用的问题
当运行到装饰器时，先自动寻找到这个同名方法并执行，参数值为装饰器下被修饰的参数
'''

def log(func_name):
    '''
    wraps 本身也是装饰器，作用就是把原函数的原信息拷贝回来
    '''
    @wraps(func_name)
    def wrapper():
        print('我是装饰器')
        logging.warning('{}正在执行'.format(func_name))
        return func_name()

    return wrapper

@log  # 装饰器
def fun1():
    print('执行函数1')


fun1()

