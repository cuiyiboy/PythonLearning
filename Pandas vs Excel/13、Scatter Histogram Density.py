#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
散点图、直方图、密度图
'''

import pandas as pd
import matplotlib.pyplot as plt
import scipy

pd.options.display.max_columns = 777  # 所有列都显示出来
homes = pd.read_excel('E:\python_learning\Pandas vs Excel\File\File13\home_data.xlsx', index_col='id')
print(homes.head())
print(homes.columns)

# 房屋面积和价格的关系：
# 直方图展示价格分布：
# 密度图，散点图

# homes.plot.scatter(x='price',y='sqft_living')       # 散点图
# plt.xticks(fontsize=8, rotation=45, ha='right')     # 设置x轴刻度

homes.sqft_living.plot.hist(bins=100)   # 直方图
plt.xticks(range(0,max(homes.sqft_living),500),fontsize=8, rotation=45)

# homes.sqft_living.plot.kde()  # 密度图
# plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=45)

plt.tight_layout()

plt.show()
