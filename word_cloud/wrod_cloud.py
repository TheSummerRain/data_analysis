# author: C.C.
# contact: 3280766842@qq.com
# datetime:2021/3/3 17:09
# software: PyCharm

"""
文件说明：
慈云帮助文档。
http://amueller.github.io/word_cloud/
"""
import jieba        #中文分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud     #词云图
from PIL import Image   #图片处理
import numpy as np  #矩阵运算
import xlwt
import xlrd
import pandas as pd
import jieba.analyse



# 导入要处理的数据文件
df = pd.read_csv("E:/wordcloud/data333.csv")

# 关键词
word  = ""
for i in df.反馈内容:
    if i != "nan":
        word = word + str(i)
word=word.replace(' ','').replace('\n','').replace('\r','').replace(';','').replace('nan','').replace('请选择在何处发生该问题:','').replace('选择你遇到的问题:','').replace('我','')
word=word.replace('怎么','').replace('了','').replace('的','').replace('为什么','').replace('吗','')
word=word.replace('啊','').replace('不','').replace('是','').replace('如果','').replace('还是','')
word=word.replace('一直','').replace('在','').replace('请问','').replace('呢','')
word=word.replace('但','').replace('自己','').replace('什么','').replace('这个','')
print(word)

# 处理数据源
# for i in df.分类:
#     if i != "nan":
#         word = word + str(i)
#
# word=word.replace(' ','').replace('\n','').replace('\r','').replace(';','')
# word=word.replace('选择你遇到的问题:','').replace('请选择在何处发生该问题:','').replace('nan','')
# word=word.replace('默认值:','').replace('无法发表','')
# print(word)



# 方案1，精准分词模式，默认cut_all=False;  当等于True时，为全模式
cut=jieba.cut(word,cut_all=True)
string=' '.join(cut)
print(string)
print(len(string))

"""
# 方案2：搜索词模式
cut=jieba.cut_for_search(word)
"""

"""
# 获取频率最高的词语
kk = jieba.analyse.extract_tags(word,topK)  #topK最高的频率词
print(kk)
"""

# exit()

# -----------------------------------------------
#导入一张白底图片
img=Image.open('E:/wordcloud/6666.jpg')
img_array=np.array(img)     #将图片转化为数组


# 词云设置
wc=WordCloud(
    background_color='white',
    width=2000,
    height=1500,
    margin=5,
    max_words=100,  # 设置最多显示的词数
    font_path="simhei.ttf",  # 中文词图必须设置字体格式，否则会乱码，这里加载的是黑体
    random_state=100
)

# 慈云关键字导入
ss  = wc.generate_from_text(string)
print()

#绘制图片
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('on')     #是否显示坐标轴

plt.show()      #显示图片
#plt.savefig('./wordcloud_summary.png',dpi=500) #保存图片 dpi表示图片清晰度


