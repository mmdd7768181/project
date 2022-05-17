class Account():
    def __init__(self, name, money):
        self.__name = name
        self.__money = money

    def get_money(self):
        return self.__money

    def set_money(self, m):  # m是操作的钱
        if (isinstance(m, int) or isinstance(m, float)):
            if 0 < m < self.__money:
                self.__money -= m
            else:
                return '余额不足'
        else:
            return '非法输入'
        return self.__money
        # print('还剩下{}金币'.format(self.__money))


xiaomin = Account('小明', 100)
# xiaomin.set_money(4)
print(xiaomin.set_money('sss'))  # 若用return，则需要使用print打印出结果
