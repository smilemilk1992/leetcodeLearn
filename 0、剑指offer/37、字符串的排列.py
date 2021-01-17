# 输入一个字符串，打印出该字符串中字符的所有排列。
#
#
#
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
#
#
#  示例:
#
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#
#
#
#
#  限制：
#
#  1 <= s 的长度 <= 8
#  Related Topics 回溯算法
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        length = len(s)
        if length == 1:
            return [s]  # 边界
        else:
            res = []
            for i in range(length):
                ch = s[i]  # 取出s中每一个字符
                rest = s[:i] + s[i + 1:]
                for x in self.permutation(rest):  # 递归
                    res.append(ch + x)  # 将ch 和子问题的解依次组合
        return list(set(res))


    def permutationList(self,lists):
        res=[]
        track=[]
        self.check(lists,track,res)
        return res

    def check(self,lists,track,res):
        if len(track)==len(lists):
            res.append(list(track))
        else:
            for li in lists:
                if li not in track:
                    track.append(li)
                    self.check(lists,track,res)
                    track.pop()

if __name__ == '__main__':
    s=Solution()
    # x = "aab"
    # f=s.permutation(x)
    # print(f)

    x=[1,2,3]
    f=s.permutationList(x)
    print(f)
