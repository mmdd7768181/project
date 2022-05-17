import pymysql
from pymysql import cursors
host = "www.hctestedu.com",
port = 3306,
user = 'api_test',
password = 'Aa9999!',
database = 'shopxo_hctested'
sqll = None


def sql_function():
    db = pymysql.connect(host=host,
                         port=port,
                         user=user,
                         password=password,
                         database=database)

    # 使用cursor()方法创建一个游标对象 cursor,并且规范输出内容为dict
    cursor = db.cursor(cursors.DictCursor)

    # 使用execute()方法执行sql查询
    cursor.execute(sqll)

    # 使用 fetchone()方法获取单条数据
    # data = cursor.fetchone()
    # # 使用 fetchall()方法获取所有数据
    data=cursor.fetchall()
    # print(data)
    db.close()  # 关闭数据库本身
    return data