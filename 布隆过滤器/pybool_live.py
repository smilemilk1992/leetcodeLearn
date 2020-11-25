# -*- coding: utf-8 -*-
"""
@File    :   pybool_live.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/11/25 11:20    1.0         None
"""
__author__ = 'haochen214934'
from pybloom_live import ScalableBloomFilter, BloomFilter

# # 可自动扩容的布隆过滤器
bloom = ScalableBloomFilter(initial_capacity=100000, error_rate=0.000001)
#
url1 = 'http://www.baidu.com'
url2 = 'http://qq.com'
#
bloom.add(url1)
print(url1 in bloom)
print(url2 in bloom)

bf = BloomFilter(capacity=1000)
bf.add(url1)
print(url1 in bf)
print(url2 in bf)