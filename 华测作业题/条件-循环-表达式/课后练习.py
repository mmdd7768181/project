# a = 0
# while True:
#     print('hello')
#     a += 1
#     if a < 3:
#         continue
#     else:
#         break

# lis = [[1, 2, 3], ['a', 'b', 'c'], ['甲', '乙', '丙', '丁']]
# for i in lis:
#     # print(lis[i])
#     for j in i:
#         print(j)
# 'url': 'www.aaa.com'
d = {'url': 'www.aaa.com', 'data': {'uname': 'admin', 'pwd': '123'}}
for i in d:
    print(d[i])
    if i == 'data':
        for j in d[i]:

            print(d[i][j])
