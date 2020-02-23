'''
函数填充
'''
import pandas as pd

books = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File05\Booksfor5.xlsx')
print(books.shape)
print(books.head())
print('======')


# 计算开始的Price
# 方法1：针对整列进行操作
books['Price'] = books['ListPrice'] * books['Discount']

# 方法2：针对一列中的部分进行操作,可以选择下面的形式
# for i in books.index:
#     books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]
#     # books.at[i,'Price'] = books.at[i,'ListPrice'] * books.at[i,'Discount']


# 计算新的PriceNew，ListPrice增加2后
books['ListPriceNew'] = books['ListPrice'] + 2
books['ListPriceNew1'] = books['ListPrice'].apply(lambda x:x+5) # 可以用lambda代替上式
# 方法1：针对整列进行操作
# books['PriceNew'] = books['ListPriceNew'] * books['Discount']

# 方法2：针对一列中的部分进行操作,可以选择下面的形式
books['PriceNew']=pd.Series()       # 提前生成一列
for i in books.index:       # for i in range(5,16)
    books['PriceNew'].at[i] = books['ListPriceNew'].at[i] * books['Discount'].at[i]
    # books.at[i,'PriceNew'] = books.at[i,'ListPriceNew'] * books.at[i,'Discount']

print(books.columns)
print(books.head())

books.to_excel('E:\python_learning\Pandas vs Excel\File\File05\Booksfor5_1.xlsx')