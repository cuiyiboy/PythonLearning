#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
定位和去重
'''
import pandas as pd

students = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File20\Students_Duplicates.xlsx')
print(students,'\n')

students_new=students.drop_duplicates(subset='Name',keep='first',inplace=False)    # subset按哪些列去重，keep='first'\'last'\False默认'first', inplace默认值为False生成新的;
print(students_new,'\n')
students_new.to_excel('E:\python_learning\Pandas vs Excel\File\File20\Students_Duplicates_0.xlsx',sheet_name='去重后数据')

# 找出重复的行数,方法1
temp1=students.duplicated(subset='Name',keep='last')   # duplicated函数：指定列数据重复项判断，返回：指定列重复行boolean Series
temp2=students.iloc[temp1[temp1].index]
print(temp2,'\n')       # 根据索引查询各行，temp[temp] 等价于 temp[temp==True]
temp2.to_excel('E:\python_learning\Pandas vs Excel\File\File20\Students_Duplicates_1.xlsx',sheet_name='重复的数据方法一')

# 找出重复的行数，方法2
temp1=students.drop_duplicates(subset='Name', keep='first')     # 去重，保留一组重复数据
temp2=students.drop_duplicates(subset='Name', keep=False)     # 去重，将重复数据丢弃
temp3=temp1.append(temp2).drop_duplicates(subset='Name', keep=False)     # 合并，去重，将重复数据丢弃
print(temp3)
temp3.to_excel('E:\python_learning\Pandas vs Excel\File\File20\Students_Duplicates_2.xlsx',sheet_name='重复的数据方法二')

# ？？？？？？？？？？？？？？研究如何写入到不同的sheet_name里面？？？？？？？？？？？？？