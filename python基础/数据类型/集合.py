"""
集合特点：无序可变，即没有索引值，所有数据不会重复
数据类型：支持数字、字符串、元组，不支持列表、字典和集合类型
set.add() 添加元素，参数只能是 数字类型和字符串
set.add() 添加元素，参数可以是字符串、列表、元组、字典、不支持数字类型，参数可以 有多个，逗号隔开
set.pop() 随机删除元素
set.remove(value) 指定删除元素，若元素不存在则会报错
set.discard(value) 指定删除元素，若元素不存在也不会报错
set.clear() 清空集合

"""
s1={'aa','bb','cc'}
s2={'aa','dd','ee','ff'}
# s1.add('baidu')
# print(s1)
#
# s1.add(1)
# print(s1)

# s1.add([1,2,3]) # 添加列表时会报错
# print(s1)

# s1.update([1,2,3]) # 运行结果：{1, 2, 3, 'aa', 'bb', 'cc'}
# print(s1)

# s1.pop()
# print(s1)

# s1.remove('aa')
# print(s1)
# s1.remove('aa1') # 删除不存在的元素时，提示：KeyError: 'aa1' 报错
# print(s1)

# s1.discard('aa1') #  删除不存在的元素时，不会报错，返回的是原先的集合{'cc', 'bb', 'aa'}
# print(s1)

"""
集合的运算：
交集：set1.intersection(set2)
并集：set1.union(set2)
差集：set1.difference(set2)
"""

# print(s1.intersection(s2))
# print(s1 & s2)
#
# print(s1.union(s2))
# print(s1 | s2)
#
# print(s1.difference(s2))
# print(s1 - s2)
# print(s2.difference(s1))
# print(s2 - s1)

"""
set(其他数据类型)-->set,且会自动去重

"""
s='hello'
l1=['cc',2,2]
t1=(1,2,'aa')
d1={'A':'daiwei','B':'hally','C':'hally'}

print(set(s))  # {'l', 'h', 'o', 'e'}
print(set(l1)) # {2, 'cc'}
print(set(t1)) # {1, 2, 'aa'}
print(set(d1)) #  {'C', 'B', 'A'} ，字典里的VALUE指顺序是反过来的

