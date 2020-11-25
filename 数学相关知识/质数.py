# -*- coding: utf-8 -*-
"""
@File    :   质数.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/11/20 10:10    1.0         None

质数（Prime number），又称素数，指在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数。（也可定义为只有1与该数本身两个正因数的数）
"""
__author__ = 'haochen214934'

#方法1的时间复杂度是O(n)。
class Solution1:
    def isPrime(self, s):
        if s<3:
            return s>1
        for i in range(3,s):
            if s%i==0:
                return False
        return True

#当一个数不是质数时，必定存在两个约数，一个大于等于sqrt(n)，另一个小于sqrt(n)。利用这种特性，可以对方法1进行改进，只判断数n能否被小于sqrt(n)的数整除。
#时间复杂度是O(sqrt(n))。
class Solution2:
    def isPrime(self, s):
        if s<3:
            return s>1

        sqrt=int(s**0.5)
        # 判断一个数能否被小于sqrt(n)的数整除
        for i in range(2,sqrt+1):
            if s%i==0:
                return False
        return True

#任一偶数一定能分解为2和其他偶数/奇数的积，因此一个数不能被2整除，那么这个数一定不能被其他偶数整除。利用这个特点，可以对方法2进行改进，判断数n能否被小于sqrt(n)的奇数整除。
#方法3的时间复杂度是O(sqrt(n)/2)。
class Solution3:
    def isPrime(self, s):
        if s<=3:
            return s>1
        sqrt=int(s**0.5)
        # 只需判断一个数能否被小于sqrt(n)的奇数整除
        for i in range(3,sqrt+1,2):
            if s%i==0 or s%2==0:
                return False
        return True


#质数的分布具有特点，经过证明可以得到，（大于等于5的）质数一定和6的倍数相邻，一定是6x-1或6x-1。利用这种特性。可以对整数进行筛选，只判断那些是6x-1或6x-1的整数是否为质数。
#方法3的时间复杂度是O(sqrt(n)/2)。
class Solution4:
    def isPrime(self, s):
        if s<=3:
            return s>1

        #只有6x-1和6x+1的数才有可能是质数
        if s%6!=1 and s%6!=5:
            return False

        sqrt=int(s**0.5)
        # 只需判断一个数能否被小于sqrt(n)的奇数整除
        for i in range(5,sqrt+1,6):
            if s%i==0 or s%(i+2)==0:
                return False
        return True


class Solution5:
    def isPrime(self, s):
        if s<3:
            return s>1
        for i in range(2, s):
            if i>5 and (s%6==5 and s%6==1):
                return True
            if s % i == 0:
                return False
        return True

if __name__ == '__main__':
    s=Solution5()
    for i in range(10):
        a =s.isPrime(i)
        if a:
            print(i)
