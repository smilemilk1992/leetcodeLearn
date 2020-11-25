# -*- coding: utf-8 -*-
"""
@File    :   redisBloom.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/11/25 11:24    1.0         None
"""
__author__ = 'haochen214934'
"""
基于redis布隆过滤器的误判率的测试
"""
import redis
from redisbloom.client import Client

pool = redis.ConnectionPool(host='127.0.0.1', port=6379,max_connections=100)
rb = Client(connection_pool=pool)
rb.bfCreate('bloom', 0.01, 1000)


rb.bfAdd('urls', 'baidu')
rb.bfAdd('urls', 'google')
print(rb.bfExists('urls', 'baidu'))  # out: 1
print(rb.bfExists('urls', 'tencent'))  # out: 0

rb.bfMAdd('urls', 'a', 'b')
print(rb.bfMExists('urls', 'google', 'baidu', 'tencent'))  # out: [1, 1, 0]