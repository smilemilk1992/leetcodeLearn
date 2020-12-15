# -*- coding: utf-8 -*-
"""
@File    :   买卖股票的最佳时机1.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/15 15:42    1.0         None
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
#  注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#  示例 1:
#
#  输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
#
#  示例 2:
#
#  输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
#
#  示例 3:
#
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
#  Related Topics 数组 动态规划
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    #最多完成两笔交易
    #动态规划 https://blog.csdn.net/qq_36512295/article/details/100782630
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for t in range(1, 3):
            min_p = prices[0]  # 初始化最小负收益，即买入初始股票
            for i in range(1, n):
                min_p = min(min_p, prices[i] - dp[t - 1][i - 1])  # 更新最小负收益
                dp[t][i] = max(dp[t][i - 1], prices[i] - min_p)  # 更新当前交易次数下第 i 天的最大收益
        return dp[-1][-1]

    #数组
    def maxProfit1(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min =prices[0]
        money=0
        i=0
        for p in prices:
            if p<=min:
                min=p
            print(p,min,money)
            if p-min>money and i%2<=1 and i<=2:
                i = i + 1
                money=money+(p-min)
        return money



if __name__ == '__main__':
    s=Solution()
    prices=[3,3,5,0,0,3,1,4]
    money=s.maxProfit(prices)
    print(money)