'''
数据筛选
'''

import pandas as pd

students = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File07\Students.xlsx', index_col='ID')
print(students.shape)
print(students)

# 注释的部分，可以用下面的lambda表达式代替
# def age_18_to_30(a):
#     return 18 <= a < 30
#
#
# def level_a(a):
#     return 85 <= a <= 100
#
#
# students = students.loc[students.Age.apply(age_18_to_30)].loc[students['Score'].apply(level_a)]  # 与下面一行一样

# 下面一行使用lambda函数，替代上面定义的函数
students = students.loc[students.Age.apply(lambda x: 18 <= x < 30)].loc[students.Score.apply(lambda x: 85 <= x <= 100)]
# students = students.loc[students['Age'].apply(lambda x: 18 <= x < 30)].loc[students['Score'].apply(lambda x: 85 <= x <= 100)]

students.sort_values(by='Score', inplace=True, ascending=False)
print(students)
