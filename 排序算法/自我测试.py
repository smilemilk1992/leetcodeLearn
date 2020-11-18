# -*- coding: utf-8 -*-
"""
@File    :   自我测试.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/9/27 17:47    1.0         None
"""
__author__ = 'haochen214934'

from typing import List


class Solution(object):
    def permute(self, nums: List[int]) -> List[int]:
        pass




if __name__ == '__main__':
    #大堆 从下往上
    # 12 10 5 6 3 4 1 2
    #小堆
    num = [4,3,2,10,12,1,5,6]
    a=Solution()
    a.permute(num)