# author: C.C.
# contact: 3280766842@qq.com
# datetime:2021/2/8 14:40
# software: PyCharm

"""
文件说明：

"""

import lxml
import requests
from lxml import etree

url = 'https://datachart.500.com/ssq/history/newinc/history.php?limit=5000&sort=0'
resp = requests.get(url)
hm = etree.HTML(resp.text)
# 在返回页面内容的任意位置查找id=tdata的tbody标签，并取其下所有的tr标签内容，赋给trs列表
trs = hm.xpath("//tbody[@id='tdata']/tr")

f = open('data.csv', 'w')  # 将攫取的数据存到data.csv文件
for tr in trs:
    data_lst = tr.xpath('td/text()')
    # 准备写入文件，以备后用，csv文件是pandas能直接读取的，最有效率
    # 去掉列表中的逗号和\xa0,使用的是列表推导式完成这个任务
    data_lst = [x.replace(',', '').replace('\xa0', '') for x in data_lst]
    f.write(','.join(data_lst) + '\n')
f.close()
