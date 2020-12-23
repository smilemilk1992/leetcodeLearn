# -*- coding: utf-8 -*-
"""
@File    :   字符串相乘.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/23 14:55    1.0         None
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
#  示例 1:
#  输入: num1 = "2", num2 = "3"
# 输出: "6"
#
#  示例 2:
#  输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
#  说明：
#  num1 和 num2 的长度小于110。
#  num1 和 num2 只包含数字 0-9。
#  num1 和 num2 均不以零开头，除非是数字 0 本身。
#  不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#  Related Topics 数学 字符串
"""
__author__ = 'haochen214934'
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" is num1 or "0" is num2:
            return "0"
        result = [0 for i in range(len(num1) - 1)]
        len_num2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        # 处理进位
        carry = [0 for i in range(len(num1) + len(num2))]
        print(carry)
        for l2 in range(len_num2):
            i = l2
            result.append(0)
            for n1 in num1:
                if carry[i] != 0:
                    # 判断之前是否有进位的情况，清空已经处理的进位
                    result[i] += carry[i]
                    carry[i] = 0
                mul = int(num2[l2]) * int(n1)
                # 判断按位相乘的积是否是个位数
                if mul > 9:
                    carry[i + 1] += mul // 10
                result[i] += (mul % 10)
                # 判断结果是否是个位数
                if result[i] > 9:
                    carry[i + 1] += result[i] // 10
                    result[i] = result[i] % 10
                i += 1
        if carry[len(result)] != 0:  # 判断最高位是否还有进位
            result.append(carry[len(result)])
        p = ''.join(str(i) for i in result)
        p = p[::-1]
        print(result)
        return p


if __name__ == '__main__':
    s=Solution()
    num1 = "123"
    num2 = "456"
    flag=s.multiply(num1,num2)
    print(flag)