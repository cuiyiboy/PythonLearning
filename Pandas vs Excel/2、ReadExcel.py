"""
读取Excel
"""
import pandas as pd

# 第几列作为列名，默认header=0， 没有列明时header=None
people = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File02\People.xlsx',
                       index_col='ID')
# people.columns = ['ID','Type','Title','FirstName','MiddleName','LastName']

print(people.shape)     # 行数、列数
print(people.columns)       # 列明
print(people.index)
print(people.head())        # 前几行
print(people.tail())        # 后几行
print('=================')
people.to_excel('E:\python_learning\Pandas vs Excel\File\File02\People2.xlsx')
print('Done!!!')