"""
定义在类中的变量，并不是在函数中
属性的值通过构造方法（__init__）传入
公有类属性：不用两个下划线开头的，都可以使用----类里面和外面都可以使用
私有类属性：用两个下划线开头的，只能在自己的类里面使用
实例名.属性命
类里面可以直接通过类名.属性
类名.公有属性
"""

class person():
    type = '人类'
    num = 0
    __phone = 13344445555

    def eat(self):
        print(person.type)
        print('爱吃是天性')

    def work(self):
        print(person.__phone)
        print('不工作就没钱')


p = person()
print(p)
p.work()
