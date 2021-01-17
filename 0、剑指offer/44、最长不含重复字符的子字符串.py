# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#
#
#
#  示例 1:
#
#  输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
#  示例 2:
#
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
#  示例 3:
#
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#
#
#  提示：
#
#
#  s.length <= 40000
#
#
#  注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-rep
# eating-characters/
#  Related Topics 哈希表 双指针 Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0
        if len(s)==1:
            return 1
        _max=0
        low=0
        high=1
        while low<high and low<len(s) and high<len(s):
            if s[high] not in s[low:high]:
                high=high+1
                _max = max(_max, len(s[low:high]))
            elif high-low==1:
                _max=max(_max,len(s[low:high]))
                low=low+1
                high=high+1
            else:
                _max=max(_max,len(s[low:high]))
                low=low+1
        return _max

if __name__ == '__main__':
    s=Solution()
    ss="pwwkew"
    f=s.lengthOfLongestSubstring(ss)
    print(f)