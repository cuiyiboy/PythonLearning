'''
创建Excel
'''
import pandas as pd

df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['X', 'Y', 'Z'], 'Score': [88, 99, 100]})
print(df)

df = df.set_index('ID')
print(df)

# df = df.set_index('Name',inplace=True)
# print(df)

df = df.to_excel('E:\python_learning\Pandas vs Excel\File\File01\output.xlsx')

print('Done!!')
