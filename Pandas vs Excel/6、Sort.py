'''
排序和多重排序
'''

import pandas as pd

products = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File06\List.xlsx', index_col='ID')
print(products)

products.sort_values(by='Price', inplace=True, ascending=False)     # 默认升序ascending=True
print(products)

products.sort_values(by=['Worthy','Price'], inplace=True, ascending=[True, False])     # 将排序的列和方式放在列表中
print(products)

products.to_excel('E:\python_learning\Pandas vs Excel\File\File06\ListNew.xlsx')
print('Done!!')