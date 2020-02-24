#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
饼图
'''

import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel("E:\python_learning\Pandas vs Excel\File\File11\\Students.xlsx", index_col='From')
print(students)

students['2017'].plot.pie(fontsize=8, counterclock=False, startangle=-270,
                          explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

plt.title('Source of International Students', fontsize=16, fontweight='bold', color='red')

plt.ylabel('2017', fontsize=16, fontweight='bold', color='red')

plt.show()