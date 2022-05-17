class Account():
    def __init__(self, name, money):
        self.__name = name
        self.__money = money

    @property
    def name1(self):
        return self.__name

    @name1.setter  # set值--私有变量
    def name1(self, n):
        self.__name = n
        return self.__name

    @property
    def money1(self):
        return self.__money

    @money1.setter
    def money1(self, m):  # m是操作的钱
        if isinstance(m, int) or isinstance(m, float):
            # self.money=m
            if 0 < m < self.__money:
                self.__money -= m
                print('现在余额是{}'.format(self.__money))
            else:
                return '余额不足'
        else:
            return '非法输入'
        return self.__money
        # print('还剩下{}金币'.format(self.__money))


xiaomin = Account('小明', 100)
print('')