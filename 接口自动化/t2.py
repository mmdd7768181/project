# -*- coding: utf-8 -*-
# author: 华测-长风老师

import pymysql
"""
pymysql 是一个外部库；
pip install pymysql

"""
"""
jdbc:mysql://www.hctestedu.com:3306/shopxo_hctested
www.hctestedu.com:3306/shopxo_hctested
在本质上，python+pymysql 是一样的连接方式；

"""

# 打开数据库连接,并且生成一个数据库对象；
db = pymysql.connect(host='shop-xo.hctestedu.com',
                     port=3306,
                     user='api_test',
                     password='Aa9999!',
                     database='shopxo_hctested')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询/增加/修改/删除；
# 一个查询/增加/修改/删除语句是否能够被执行；取决于你的账号是否具有对应权限
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

# 使用 fetchall() 方法获取所有数据.
# data = cursor.fetchall()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()

"""
python+pymysql 会创建两个对象： 数据库对象、游标对象；
数据库对象是用来管理数据库本身的；
游标对象是用来执行操作语句的；这里也就不难理解为什么，获取执行语句结果需要用到游标对象；
"""



