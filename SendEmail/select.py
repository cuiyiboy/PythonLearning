# -*- coding:utf-8 -*-
# mysql连接函数

import pymysql
import xlwt

# 连接数据库
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="cuiyi211314",
                       port=3306)

# 通过cursor创建游标
cursor = conn.cursor()

# 写sql，执行数据查询
sql = 'select * from salary.money'
cursor.execute(sql)
results = cursor.fetchall()

# 关闭数据连接
conn.close()

excel = xlwt.Workbook()  # 创建excel文件
sheet = excel.add_sheet('results')  # 创建一个sheet页
title = ['id', 'name', 'sex', 'addr', 'age']

# 写表头
i = 0
for header in title:
    sheet.write(0, i, header)
    i = i + 1

# 写数据
for row in range(0, len(results)):
    for col in range(0, len(results[row])):
        sheet.write(row+1, col, results[row][col])
        col += 1
    row += 1

# 保存数据
excel.save('E:\python_learning\SendEmail\data\\results.xls')
print('导出成功！')
