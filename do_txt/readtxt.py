"""
# 本文档专门用来处理，新CMS日志统计的问题。
# 可以将技术那边的日志格式，转换为：excle格式
"""

import pandas as pd
import time

print("====开始=====", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
listAll = []

"""
# 修改这个文件名即可自动生成excle.
"""
filename = "20210415"


# 格式化基础日志文件
with open("bi-audit-statistics-" + filename + ".log", "r", encoding='UTF-8') as f:  # 打开文件
    while True:
        data = f.readline()  # 读取文件
        if not data:
            print("data=", data)
            break
        # 数据组装，以“[”开头的数据，加入列表。但是对数据进行中英文格式化，同时分组。最后使用pd写入excle.
        if data.startswith("["):
            listAll.append(data.replace("[", "").replace("]", "").replace("\n", "").replace("refuse", "拒绝操作").replace(
                "pageChapterPending", "待审核").replace("pageChapterRetrialRefused", "被动改").replace("signed",
                                                                                                 "通过").replace(
                "type_chapter",
                "章节审核").replace("pageBookPicApply", "待审核").replace("pageBookPicRefused", "已拒绝").replace(
                "pageChapterRetrialInitiative", "主动改").replace("pageIntroPending", "待审核").replace("pageIntroRefused",
                                                                                                  "已拒绝").replace(
                "type_book_cover", "书封审核").replace("type_book_intro",
                                                   "简介审核").replace(
                "type_new_book", "新书审核").replace("pageNewBookPending",
                                                 "待审核").replace(
                "pageNewBookRetrial", "重审核").replace("pageNewBookRefused", "已拒绝").replace("pageChapterRefused",
                                                                                          "已拒绝").split(" "))

# pd写入excle
dataframe = pd.DataFrame(listAll)
print(dataframe)
dataframe.to_excel('D:/PythonProject/data_analysis/do_txt/' + filename + '.xlsx')  # 注意后缀格式。
print("====结束=====", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
