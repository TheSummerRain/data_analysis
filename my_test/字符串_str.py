# author: C.C.
# contact: 3280766842@qq.com
# datetime:2021/2/22 13:22
# software: PyCharm

"""
文件说明：
讲解各种字符串的操作。
"""


a = "hello,alix!"

#切片 - 顾头不顾尾。
print(a[1:3])  # el

# 打印一种特别的样式
print(a.center(30,"-"))   # ---------hello,alix!----------


#判断字符串开头，结尾
print(a.endswith("A"))  # False
print(a.startswith("h")) # True


#
