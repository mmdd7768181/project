"""
数组可以增删改查
元组只可以查
字典

"""

l1=[1,2,3]
l2=['a','b','c']

# l1.append(l2)
# print(l1[::-1])
# for i in l2:
#     print(l1.extend(i))


# for i in l2:
#     print(i,end=' ')
l2.extend(l1) # extend 后面不能直接加数字，会报错
print(l2)

d1 = {'节目': '好声音', '导师': ['杨坤', '那英'], '学员': {'A组': '豆豆', 'B组': '爱爱'}}
# print(d1['节目'])
# d1['节目']='中国好声音'
# print(d1)
# d1.pop(['导师'][0])
# print(d1)
# d1['学员']['A组']='美美'
# print(d1)
# d1['导师'].remove('杨坤')   # 嵌套删除，利用数组的 remove 删除方法
# print(d1)

# print(d1.items())
# print(d1.keys())
# print(d1.values())
# d2=d1.copy()
# print(d2)
# for i in d2:
#     print(i)
# print(d1.get('节目1'))

