# -*- coding: utf-8 -*-
"""
@File    :   买卖股票的最佳时机1_允许一次.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/15 15:42    1.0         None
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
#  如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#
#  注意：你不能在买入股票前卖出股票。
#
#  示例 1:
#
#  输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#
#
#  示例 2:
#
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#  Related Topics 数组 动态规划
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    #最多一次交易
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min =prices[0]
        money=0
        for p in prices:
            if p<=min:
                min=p
            if p-min>money:
                money=p-min
        return money

    #改进
    def maxProfit1(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minprice=float('inf')
        maxprofit=0
        for p in prices:
            minprice = min(p,minprice)
            maxprofit =max(maxprofit,p-minprice)
        return maxprofit


    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0
            # 初始化状态
        n = len(prices)
        dp=[0]*n
        minprice=prices[0]
        for i in range(1,n):
            minprice=min(minprice,prices[i])
            dp[i]=max(dp[i-1],prices[i]-minprice)
        return dp[-1]


if __name__ == '__main__':
    s=Solution()
    prices=[7,1,5,3,6,4]
    money=s.maxProfit2(prices)
    print(money)