import pymysql

db = pymysql.connect(host="www.hctestedu.com",
                     port=3306,
                     user='api_test',
                     password='Aa9999!',
                     database='shopxo_hctested')

# 使用cursor()方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用execute()方法执行sql查询
cursor.execute('SELECT VERSION()')

# 使用 fetchone()方法获取单条数据
data = cursor.fetchone()
# # 使用 fetchall()方法获取所有数据
# data=cursor.fetchall()

print('Database version:%s' % data)

db.close()  # 关闭数据库本身
