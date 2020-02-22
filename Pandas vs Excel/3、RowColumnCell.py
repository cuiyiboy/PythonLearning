"""
行、列、单元格
"""
import pandas as pd

s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[4, 5, 6], name='C')

df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})  # 字典形式
print(df)
print('============')

df = pd.DataFrame([s1, s2, s3])  # 列表形式
print(df)
