#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
柱状图
'''

import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File08\Students.xlsx')

students.sort_values(by='Number', inplace=True, ascending=False)      # 先排序，再作图

plt.bar(students.Field, students.Number, color='orange')  # 柱形图颜色

plt.xticks(students.Field, rotation=45, ha='right')  # X轴旋转
# plt.yticks(students.Number, rotation=45, ha='right')    # Y轴旋转，基本不用

plt.xlabel('xlable', fontsize=15, fontweight='bold', color='blue')  # X轴名称

plt.ylabel('ylable', fontsize=15, fontweight='bold', color='blue')  # Y轴名称

plt.title('bbbbbbbbbb', fontsize=30, fontweight='bold', color='red')  # 标题及大小

plt.tight_layout()

plt.show()
