# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈
# 的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
#
#  示例 1：
#  输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
#  示例 2：
#  输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出。
#
#  提示：
#  0 <= pushed.length == popped.length <= 1000
#  0 <= pushed[i], popped[i] < 1000
#  pushed 是 popped 的排列。
from typing import List

'''
借用辅助栈模拟出栈过程；
遍历入栈元素，添加到辅助栈；
当辅助栈不空，且栈顶元素等于popped的元素时，辅助栈弹出，popped元素加1；
如果不等，则继续添加元素至辅助栈，直到pushed为空；
判断此时stack是否pop完成。
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i = i + 1
        return not stack

if __name__ == '__main__':
    s=Solution()
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    f=s.validateStackSequences(pushed,popped)
    print(f)
