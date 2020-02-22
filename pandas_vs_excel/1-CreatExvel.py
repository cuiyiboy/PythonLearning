import pandas as pd

df = pd.DataFrame({'ID': [0, 1, 2, 3], 'name': ['Mark', 'Tomi', 'Jack', 'Cuiyi']})
print(df)

df = df.set_index('ID')     # 此处设置数据表的索引，如未设置索引会自动在最前方添加一列作为索引
# df = df.set_index('ID',inplace=True)      # 在原来的 DataFrame 上进行修改
print(df)

df.to_excel('E:\python_learning\pandas_vs_excel\EXCEL\output.xlsx')