# -*- coding: utf-8 -*-
"""
@File    :   括号生成.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/11 14:10    1.0         None
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  示例：
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#
#  Related Topics 字符串 回溯算法
"""
__author__ = 'haochen214934'

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.backtrack(res,"",0,0,n)
        return res

    def backtrack(self,res,cur,open,close,max):
        if len(cur)==max*2:
            res.append(cur)
        if open<max:
            self.backtrack(res,cur+"(",open+1,close,max)
        if close<open:
            self.backtrack(res,cur+")",open,close+1,max)



if __name__ == '__main__':
    s=Solution()
    n=3
    f=s.generateParenthesis(n)
    print(f)