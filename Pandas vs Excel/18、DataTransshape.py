#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
分裂
'''

import pandas as pd

employees = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File18\Employees.xlsx')
print(employees)

employees['First_name'] = employees['Full Name'].str.split('-', expand=True)[0]
employees['Last_name'] = employees['Full Name'].str.split('-', expand=True)[1].str.upper()

employees.to_excel('E:\python_learning\Pandas vs Excel\File\File18\EmployeesNew.xlsx')

print(employees)
