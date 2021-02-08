# author: C.C.
# contact: 3280766842@qq.com
# datetime:2021/2/8 14:41
# software: PyCharm

"""
文件说明：

"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', header=None)

# 提取红球开奖号码，在1-6列上
red_ball = df.loc[:, 1:6]  # 红球开奖号码在第1－6列上，提取所有行
# 统计红球各个开奖号码出现的次数
red_count = pd.value_counts(red_ball.values.flatten())

# 提取蓝球出现的次数
blue_ball = df.loc[:, 7]
# 统计蓝球各个开奖号码出现的次数
blue_count = pd.value_counts(blue_ball.values.flatten())

# 可视化
plt.pie(red_count, labels=red_count.index, radius=1, wedgeprops={'width': 0.3})
plt.pie(blue_count, labels=blue_count.index, radius=0.5, wedgeprops={'width': 0.3})
plt.show()
