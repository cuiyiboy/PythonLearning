import pandas as pd
from datetime import date, timedelta

# --数据区域的读取--
    # skiprows: 从序号为3的行开始读取(类似于 header)
    # usecols： 读取列的范围
    # dtype: 设置每一列的数据类型
books = pd.read_excel('E:\python_learning\pandas_vs_excel\EXCEL\Books.xlsx', skiprows=3, usecols='C:F',
                      dtype={'ID': str, 'Name': str, 'InStore': str, 'Date': str})
print(books, '\n')

# --填充整数、文字、日期--
# def add_month(d, montn_delta):
#     year = montn_delta / 12
#     month = d.month + montn_delta % 12
#     if month != 12:
#         year = year + month % 12
#         month = month % 12
#     return date(d.year + year, month, d.dsy)

start = date(2018, 10, 7)

for i in books.index:
    books['ID'].at[i] = i + 1
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'
    books['Date'].at[i] = start + timedelta(days=i)
print(books)

books.set_index('ID')
books.to_excel('E:\python_learning\pandas_vs_excel\EXCEL\Books_output.xlsx')
print('----------Done----------')
