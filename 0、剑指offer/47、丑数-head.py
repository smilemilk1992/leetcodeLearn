# -*- coding: utf-8 -*-
"""
@File    :   47、丑数-head.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/18 17:15    1.0         None
# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
#
#  示例:
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
#  说明:
#
#  1 是丑数。
#  n 不超过1690。
#
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/
#  Related Topics 数学
官方题解里提到的三个指针p2，p3，p5，但是没有说明其含义，实际上pi的含义是有资格同i相乘的最小丑数的位置。
这里资格指的是：如果一个丑数nums[pi]通过乘以i可以得到下一个丑数，那么这个丑数nums[pi]就永远失去了同i相乘的资格（没有必要再乘了），
我们把pi++让nums[pi]指向下一个丑数即可。
不懂的话举例说明：
一开始，丑数只有{1}，1可以同2，3，5相乘，取最小的1×2=2添加到丑数序列中。
现在丑数中有{1，2}，在上一步中，1已经同2相乘过了，所以今后没必要再比较1×2了，我们说1失去了同2相乘的资格。
现在1有与3，5相乘的资格，2有与2，3，5相乘的资格，但是2×3和2×5是没必要比较的，因为有比它更小的1可以同3，5相乘，所以我们只需要比较1×3，1×5，2×2。
依此类推，每次我们都分别比较有资格同2，3，5相乘的最小丑数，选择最小的那个作为下一个丑数，假设选择到的这个丑数是同i（i=2，3，5）相乘得到的，
所以它失去了同i相乘的资格，把对应的pi++，让pi指向下一个丑数即可。
"""
__author__ = 'haochen214934'
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res=[1]
        if n==1:
            return len(res)
        if n==0:
            return 0
        i=1
        while True:
            if i%2==0 or i%3==0 or i%5==0:
                res.append(i)
            if len(res)==(n if n<=10 else n+1):
                break
            i=i+1
        return res

if __name__ == '__main__':
    s=Solution()
    n=16
    f=s.nthUglyNumber(n)
    print(f)
