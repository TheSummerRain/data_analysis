# author: C.C.
# contact: 3280766842@qq.com
# datetime:2021/3/3 18:50
# software: PyCharm

"""
文件说明：

"""
import jieba        #中文分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud     #词云图
from PIL import Image   #图片处理
import numpy as np  #矩阵运算
import xlwt
import xlrd
import pandas as pd


# 导入要处理的数据文件
df = pd.read_csv("E:/wordcloud/data (5).csv")
print(df)

# df.content.apply(chinese_word_cut)


