#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
表连接
'''

import pandas as pd
import xlrd

data_path='E:\python_learning\Pandas vs Excel\File\File16\Student_Score.xlsx'  # 文件路径
Student_Score=xlrd.open_workbook(data_path)     # 使用xlrd读取文件
print(Student_Score.sheet_names())      # 使用xlrd读取文件的sheet

df=pd.read_excel(data_path,None)     # pd读取文件的sheet名
print(df.keys())

students=pd.read_excel(data_path, sheet_name='Students',index_col='Students_ID')
scores=pd.read_excel(data_path, sheet_name='Scores',index_col='Scores_ID')
print(students)
print(scores)

# merge左连接
new_table=students.merge(scores, how='left', left_on=students.index, right_on=scores.index).fillna(0)
new_table.Score=new_table.Score.astype(int)
print(new_table)

# join左连接
new_table=students.join(scores, how='left').fillna(0)
new_table.Score=new_table.Score.astype(int)
print(new_table)




