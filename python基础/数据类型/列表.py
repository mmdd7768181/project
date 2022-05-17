"""
查：
list[索引值] :单个元素的获取
list[start:end:step] ：多个元素的切片取值
"""

l1=[7,8,9,'ddd']
l2=['a','a','c','d']


# print(l1[1])

# print(l2[0:2:1])
"""
增：
List.append(value): 在原列表的尾部追加值，每次只能添加一个元素
list.insert(索引值，新值)： 在原列表的指定位置前添加元素
list1.extend(list2): 将 list2 的元素添加到 list1 中，效果等同于列表相加
"""
# l1.append('hello')
# print(l1)

# l1.insert(1,'ddd')
# print(l1)

# l1.extend(l2)
# print(l1)

"""
删：
list.remove(元素值) :在原列表中根据值删除，从左到右找到第一个删除
List.pop(索引值) :根据索引值删除元素,不加索引值，默认删除最后一个元素
list.clear() : 清空列表
del list[索引值] : 根据索引值删除单个/多个元素(切片方法)
"""

# l1.remove('ddd')
# print(l1)

# l1.pop()
# print(l1)
#
# l1.pop(1)
# print(l1)

# l1.clear()
# print(l1)

# del l1[1]
# print(l1)

# del l1[1:3]   # 返回 [7, 'ddd']
# print(l1)

"""
改：
list[索引值]=新值 ：根据索引值修改元素值
"""
# l1[1]='dsdc'
# print(l1)

# l1[1:3]='dsdc' # 输出 [7, 'd', 's', 'd', 'c', 'ddd']
# print(l1)

# l1[1:3]=['dsdc']  #输出 [7, 'dsdc', 'ddd']
# print(l1)

"""
其他方法：
list.reverse(): 反转列表
list.index(元素值) ：根据元素值来定位索引值
list.count(元素值):统计列表中该元素的个数

list(其他类型) ：强制转化为列表，必须可以被循环的元素才能转换
"""
# l1.reverse()
# print(l1)
# print(l1.index(7))
# print(l2.count('a'))