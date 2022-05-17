# # 猜数字游戏
# num1 = int(input('要猜的数字为：'))
# num2 = int(input('请输入你的数字'))
# a = 0
# if num2 > num1:
#     print('输入大了')
#
# elif num2 < num1:
#     print('输入小了')
#
# else:
#     print('输入正常')
#
# # (选做：可以控制每位玩家的猜数字次数，例如，一个人只能猜3次，3次猜错结束程序,显示正确的数字后，重新开始)
# while True:
#     if num1 == num2:
#         print('猜对啦，正确的数字为{}'.format(num2))
#         break
#     else:
#         num2 = int(input('请继续输入数字'))
#         a += 1
#         if a > 1:
#             print('次数已用完，退出程序')
#             break

# # 提示用户输入他的年龄, 程序进行判断
# age = int(input('请输入年龄'))
# if age < 10:
#     print('小屁孩')
# elif age < 20:
#     print('青春期叛逆的小屁孩')
# elif age < 30:
#     print('开始定性, 开始混社会的小屁孩儿')
# elif age < 40:
#     print('看老大不小了, 赶紧结婚小屁孩儿')
# elif age < 50:
#     print('家里有个不听话的小屁孩儿')
# elif age < 60:
#     print('自己马上变成不听话的老屁孩儿')
# elif age < 70:
#     print('活着还不错的老屁孩儿')
# elif age < 90:
#     print('人生就快结束了的一个老屁孩儿')
# else:
#     print('再见了这个世界')
#
# # 用户输入一个分数. 根据分数来判断⽤户考试成绩的档次
# score = int(input('请输入分数'))
# if score >= 90:
#     print('档次为：A')
# elif score >= 80:
#     print('档次为：B')
# elif score >= 70:
#     print('档次为：C')
# elif score >= 60:
#     print('档次为：D')
# else:
#     print('档次为：E')
#
# # 使用while循环输出1 2 3 4 5 6 8 9 10
# s = 1
# while s < 11:
#     print(s)
#     s += 1

# 用户登陆（三次机会重试）
# username = 'admin'
# b = 0
# sname = input('请输入用户名')
# while True:
#     if username == sname:
#         print('输入的用户名正确')
#         break
#     else:
#         sname = input('请继续输入用户名')
#         b += 1
#         if b > 1:
#             print('次数已用完，程序终止')
#             break



