# -*- coding: utf-8 -*-
"""
@File    :   划分字母区间.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/22 16:31    1.0         None
# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
#
#  示例：
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#
#  提示：
#
#  S的长度在[1, 500]之间。
#  S只包含小写字母 'a' 到 'z' 。
#  Related Topics 贪心算法 双指针
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    #划分尽可能多片段-双指针
    '''
    那么，这里我们遍历给定的字符串时，应该找字母最后出现的位置，因为只有这个字母最后出现的位置后切分，这个字母才能被划分为同一片段中。
    这里说下具体的做法：
    首先用哈希字典记录字符串中每个字母出现的位置（key 存在于字典则更新 value 为最远位置）；
    定义双指针 start、end，初始指向字符串的开始位置；
    遍历给定的字符串，确认每个字符的最远位置，移动 end 指针：
    若当前字符出现最远位置比前面不同字符最远位置大时，这时候要更新这个最远的位置，只有这样才能把当前字符划分到同个片段。
    当遍历的位置即是最远的位置时，表示此片段已经确认，可以切分，长度为 end-start+1，将其放到结果列表中。更新 start = end+1，继续寻找可划分片段。
    重复直至字符串遍历完成。
    '''
    def partitionLabels(self, S: str) -> List[int]:
        # 声明哈希字典存储字符出现最远位置
        char_pos = {}
        for i in range(len(S)):
            char_pos[S[i]] = i
        # 定义双指针
        start = 0
        end = 0
        # 记录最远位置
        chr_max_pos = 0
        ans = []
        # 遍历字符串
        while end < len(S):
            # 当前字符出现的最远的位置
            cur_char_max_pos = char_pos[S[end]]
            # 比较，取最远的位置，确保字符被包含在同个片段
            chr_max_pos = max(chr_max_pos, cur_char_max_pos)
            # 如果 end 在最远的位置，表示前面的所有字符都仅出现在这部分，可以切分
            if end == chr_max_pos:
                ans.append(end - start + 1)
                # 更新 start 的位置，查找下一个片段
                start = end + 1
            end += 1
        return ans


    #贪心算法 rindex() 返回子字符串 str 在字符串中最后出现的位置
    def partitionLabels1(self, S: str) -> List[int]:
        i = 0
        res = []
        while i < len(S):
            start = i
            end = S.rindex(S[i])

            for j in range(i, len(S)):
                last = S.rindex(S[j])
                if last > end:
                    end = last
                if j == end:
                    res.append(end - start + 1)
                    i = end + 1
                    break
        return res

if __name__ == '__main__':
    s=Solution()
    S = "ababcbacadefegdehijhklij"
    flag=s.partitionLabels1(S)
    print(flag)