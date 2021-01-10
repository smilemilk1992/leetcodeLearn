# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
#
#
#
#  示例 1：
#
#  输入：s = "We are happy."
# 输出："We%20are%20happy."
#
#
#
#  限制：
#
#  0 <= s 的长度 <= 10000

class Solution:
    def replaceSpace(self, s: str) -> str:
        res=""
        for i in s:
            if i is " ":
                res=res+"%20"
            else:
                res = res+i
        return res



if __name__ == '__main__':
    s=Solution()
    strs = "We are happy."
    s.replaceSpace(strs)