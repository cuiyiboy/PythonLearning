#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
叠加柱状图
'''

import pandas as pd
import matplotlib.pyplot as plt

users=pd.read_excel("E:\python_learning\Pandas vs Excel\File\File10\\Users.xlsx",index_col='ID')
users['Total']=users['Nov']+users['Dec']+users['Oct']
users.sort_values(by=['Total','Dec','Nov','Oct'], inplace=True, ascending=True)
print(users)


users.plot.barh(x='Name', y=['Oct','Nov','Dec'], color=['r','y','b'], stacked=True)   # barh:叠加水平柱状图
plt.title('User Behavior StackedHorizontal', fontsize=20, color='red', fontweight='bold')    # 标题设置：大小、颜色、加粗


users.plot.bar(x='Name', y=['Oct','Nov','Dec'], color=['r','y','b'], stacked=True)   # barh:叠加柱状图
plt.title('User Behavior Stacked', fontsize=20, color='red', fontweight='bold')    # 标题设置：大小、颜色、加粗
plt.gca().set_xticklabels(users['Name'], rotation=45, ha='right',fontsize=10, color='red', fontweight='bold')   # X轴标签设置：大小、颜色、加粗


plt.tight_layout()

plt.show()