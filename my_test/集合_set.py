# author: C.C.
# contact: 3280766842@qq.com
# datetime:2021/2/22 13:27
# software: PyCharm

"""
文件说明：

"""
import codecs
start,end = (0x4E00, 0x9FA5)
i = 0
with codecs.open("chinese.txt", "wb", encoding="utf-8") as f:
 for codepoint in range(int(start),int(end)):
  f.write(chr(codepoint))
  i = i+1
  print("第",i,"个：",chr(codepoint))
