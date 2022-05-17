"""
解析excel

"""

import xlrd,xlwt

# e = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\excel_1.xls")
# print(e.sheets()[0])

f = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\t1.xls")
print(f.sheet_names())
