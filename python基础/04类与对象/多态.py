"""
为不同的数据类型提供统一的接口
相同的内容传给不同类别的对象
根据对象的不同，产生不同的行为
"""


class payment():
    def pay(self):
        print('给钱')


class wechat(payment):
    def pay(self):
        print('微信支付')
        print('打开微信，扫码支付')


class ali(payment):
    def pay(self):
        print('支付宝支付')
        print('打开支付宝，扫码支付')


class card(payment):
    def pay(self):
        print('信用卡支付')
        print('使用pos机支付')


class startpay(): # 要操作的对象丢进来
    def pay(self, obj):
        obj.pay()


p = ali()
s = startpay()
s.pay(p)
