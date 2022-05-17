'''
open函数用法：
读用read（全部读取）、readline（只读取一行）、readlines（全部读取，返回的是列表）
写用w(会全部抹去之前的内容，只保留重新写入的内容)、a(追加，会保留之前的全部内容，并且也保留重新写入的内容)
运行代码后最好加个close函数，可释放内存
'''

file = open(r'C:\Users\Administrator\Desktop\office\t1.txt', 'a')


file.write('\nbbb')



file.close()