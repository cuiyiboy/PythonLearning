'''
读取任意区域数据，并填充
'''
import pandas as pd
from datetime import date, timedelta


def add_month(start_date, month):
    '''
    某个日期，增加某个月份后的日期
    :param start_date: 开始日期, 举例：date(2019,1,1)
    :param month: 增加的月份
    :return: 增加后的日期
    '''
    yd = month // 12
    md = start_date.month + month % 12
    if md != 12:
        yd = yd + md // 12
        md = md % 12
    return date(start_date.year + yd, md, start_date.day)


print(add_month(date(2019, 3, 1), 9))

books = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File04\Books.xlsx')
print(books)

books = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File04\Books.xlsx', skiprows=3, usecols='C:F',
                      dtype={'ID': str, 'InStore': str, 'Date': str})
print(books)

start_time = date(2019, 1, 1)
for i in books.index:
    books.at[i, 'ID'] = i + 1
    books.at[i, 'InStore'] = 'Yes' if i % 2 == 0 else 'No'
    books.at[i, 'Date'] = start_time + timedelta(days=i)
    # books.at[i,'Date'] = date(start_time.year+i, start_time.month, start_time.day)       # 按年加
    # books.at[i,'Date'] = add_month(start_time,i)       # 按月加

# for i in books.index:    # y与上面的for循环类似，两种写法
#     books['ID'].at[i] = i+1
#     books['InStore'].at[i] = 'Yes' if i%2==0 else 'No'
#     books['Date'].at[i] = start_time + timedelta(days=i)
#     # books['Date'].at[i] = date(start_time.year+i, start_time.month, start_time.day)       # 按年加
#     # books['Date'].at[i] = add_month(start_time,i)       # 按月加

books.set_index('ID', inplace=True)
books.to_excel('E:\python_learning\Pandas vs Excel\File\File04\Books1.xlsx')
print('Done')
