"""
一旦try中代码出现异常，就会执行except中的代码


"""

import logging


def jsuan(m, n):
    try:
        result = m / n
        return result
    except Exception:
        logging.error('日志记录，出错了')
        return '出现异常'


rs = jsuan(2, 'x')
print(rs)
