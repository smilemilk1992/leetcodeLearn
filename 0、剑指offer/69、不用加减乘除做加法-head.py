# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
#
#
#
#  示例:
#
#  输入: a = 1, b = 1
# 输出: 2
#
#
#
#  提示：
#
#
#  a, b 均可能是负数或 0
#  结果不会溢出 32 位整数

class Solution:
    #sum 和 carry 分别代表 位相加不进位的二进制结果 和 仅有进位的二进制结果
    def add(self, a: int, b: int) -> int:
        a = a & 0xffffffff
        b = b & 0xffffffff

        while b != 0:
            carry = ((a & b) << 1) & 0xffffffff
            a = a ^ b
            b = carry

        return a if a < 0x80000000 else ~(a ^ 0xffffffff)

    def add1(self,a,b):
        while b!=0:
            tempSum=a^b
            carrySum=(a&b)<<1
            a=tempSum
            b=carrySum

        return a

if __name__ == '__main__':
    s=Solution()
    a = -1
    b = 2
    f=s.add1(a,b)
    print(f)