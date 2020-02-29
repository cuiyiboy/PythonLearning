#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
数据的相关性
'''

import pandas as pd

pd.options.display.max_columns = 20    # 所有列都显示出来
aa=pd.read_excel('E:\\python_learning\\Pandas vs Excel\\File\\File14\\analyse.xls')

print(aa.head())

print(aa.corr())

aa.corr().to_excel('E:\\python_learning\\Pandas vs Excel\\File\\File14\\result.xlsx')

