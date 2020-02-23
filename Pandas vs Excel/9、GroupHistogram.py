#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
分组柱状图
'''

import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File09\Students.xlsx')
students.sort_values(by='2017', inplace=True, ascending=False)
print(students)

students.plot.bar(x='Field', y=['2016', '2017'], color=['red', 'black'])  # 作图及颜色
# plt.bar(x=students['Field'], y=[students['2016'], students['2017']], color=['red', 'black'])  # 该行替代不了上一行

plt.title('bbbbbbbbbb', fontsize=20, color='red', fontweight='bold')  # 标题设置：大小、颜色、加粗

plt.xlabel('Xlable', fontsize=10, color='red', fontweight='bold')  # X轴名称设置：大小、颜色、加粗

plt.ylabel('Ylable', fontsize=10, color='red', fontweight='bold')  # Y轴名称设置：大小、颜色、加粗

plt.gca().set_xticklabels(students['Field'], rotation=45, ha='right', fontsize=10, color='red',
                          fontweight='bold')  # X轴标签设置：大小、颜色、加粗

plt.gcf().subplots_adjust(left=0.01, bottom=0.1)  # 图表位置设置

plt.tight_layout()

plt.show()
