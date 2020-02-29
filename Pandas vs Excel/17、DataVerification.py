#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
数据验证
'''

import pandas as pd


def score_validation1(row):
    try:
        assert 0 <= row.Score <= 100
    except:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')


def score_validation2(row):
    if not 0 <= row.Score <= 100:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')


students = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File17\Students.xlsx')
print(students)

students.apply(score_validation1, axis=1)
print('---------------------------------')
students.apply(score_validation2, axis=1)
