class hero(object):
    name = '英雄名称'
    desc1 = '技能1'
    desc2 = '技能2'
    desc3 = '技能3'
    type1 = '英雄类型'

    def __init__(self, name, desc1, desc2, desc3, type1):
        self.name = name
        self.desc1 = desc1
        self.desc2 = desc2
        self.desc3 = desc3
        self.type1 = type1

    def a(self):
        print('{}平A一下'.format(self.name))

    def jineng1(self):
        print('{}释放技能-->{}'.format(self.name, self.desc1))

    def jineng2(self):
        print('{}释放技能-->{}'.format(self.name, self.desc2))

    def jineng3(self):
        print('{}释放技能-->{}'.format(self.name, self.desc3))

    def d(self):
        print('该英雄的类型为{}'.format(self.type1))


# dianwei = hero('典韦', '加速', '减速', '加防御', '坦克')
# print(dianwei.desc2)
# dianwei.a()
# dianwei.jineng1()
# dianwei.jineng2()
# dianwei.jineng3()
# dianwei.d()
print(hero.__name__)
print(hero.__dict__)
print(hero.__init__)