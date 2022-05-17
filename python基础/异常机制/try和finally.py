"""
try
    代码块
finally:
    代码块（不管是否异常，都会执行）

"""

import logging


def jsuan(m, n):
    try:
        result = m / n
        print('除法执行结束')

        return result
    except Exception:
        logging.error('日志记录，出错了')
        return '出现异常'

    finally:
        print('释放掉资源。。不管有无异常，都会执行')


rs = jsuan(2, 0)
print(rs)
