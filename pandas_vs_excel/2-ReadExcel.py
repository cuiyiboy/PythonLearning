import pandas as pd

people = pd.read_excel('E:\python_learning\pandas_vs_excel\EXCEL\People.xlsx')      # index_col: 指定数据的索引列

shape = people.shape        # 读取文件的行数和列数
print("shape:", shape)

columns = people.columns        #d读取文件的行（表头），不会显示索引列
print(columns)

people1 = pd.read_excel('E:\python_learning\pandas_vs_excel\EXCEL\People.xlsx', head=1)     # 当标题行上有坏数据时可使用 head 参数
print(people1.columns)

people2 = pd.read_excel('E:\python_learning\pandas_vs_excel\EXCEL\People.xlsx', head=None)     # 当标题行上有坏数据时可使用 head 参数
print(people2.columns)

head = people.head()        # 读取文件的前几行（默认为5，可传入指定行数）
print("head：\n", head)

trail = people.tail()       # 读取文件的后几行（默认为5，可传入指定行数）
print("trail: \n", trail)