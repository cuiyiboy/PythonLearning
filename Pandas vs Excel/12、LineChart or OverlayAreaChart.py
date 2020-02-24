#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
折线图、叠加面积图
'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体，SimHei

weeks = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File12\Orders.xlsx', index_col='Week')
print(weeks.head(10))
print(weeks.columns)

weeks.plot(y=['Accessories','Bikes','Clothing','Components'])   # 折线图
# weeks.plot.area(y=['Accessories','Bikes','Clothing','Components'])    # 叠加面积图
# weeks.plot.bar(y=['Accessories','Bikes','Clothing','Components'], stacked=True)    # 叠加区域图
plt.title('States Weekly Trend', fontsize=16, fontweight='bold', color='blue')   # 设置标题的名称、字体大小、颜色
plt.ylabel('Total', fontsize=12, fontweight='bold')     # 设置y轴标签
plt.xticks(weeks.index, fontsize=8, rotation=0, ha='right')     # 设置x轴刻度


plt.show()
