#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
分裂
'''

import pandas as pd

students=pd.read_excel('C:\Python\learn\Pandas vs Excel\File\File19\Students.xlsx',index_cole='ID')
print('students:\n',students)

temp=students[['Test_1','Test_2','Test_3']]     # 创建一个临时的DataFrame,包括运算设计到的列；
students['Total']=temp.sum(axis=1)      # axis=1,按行计算；不写就是默认axis=0，按列计算；
students['Mean']=temp.mean(axis=1)
students['XXX']=students.Test_1+students.Test_2-students.Test_3

col_mean=students[['Test_1','Test_2','Test_3','Total','Mean','XXX']].mean()     # 创建一个临时DataFrame,再默认按列求平均；
# col_mean['Name'],col_mean['ID']='Summary',21     # 创建Name、ID列，并赋值；
col_mean['Name']='Summary'      # 创建Name列，并赋值；
col_mean['ID']=21      # 创建ID列，并赋值；
# print('col_mean:\n',col_mean)
students=students.append(col_mean, ignore_index=True)       # 将案列计算的值append进原数据列


print('students:\n',students)
students.to_excel('C:\Python\learn\Pandas vs Excel\File\File19\Students_New.xlsx',index=False)
