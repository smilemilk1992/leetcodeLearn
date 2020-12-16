# -*- coding: utf-8 -*-
"""
@File    :   输出所有和为S的连续正数序列.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/10/13 15:33    1.0         None

题目描述：
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序


思路：
大体的思路为设定两个指针start,end表示序列的最小值和最大值，
当序列的相加的值大于给定的sum值时，我们需要减去start对应的值，
并递增start，否则，我们应该递增end
"""
__author__ = 'haochen214934'

#滑动窗口
class Solution:
    def FindContinuousSequence(self, sum: str) -> int:
        #存放结果
        result=[]
        plow=1
        phigh=2
        if sum<3:
            return result
        while plow<phigh:
            cur=(plow+phigh)*(phigh-plow+1)/2
            lists=[]
            #相等，那么就将窗口范围的所有数添加进结果集
            if cur==sum:
                for i in range(plow,phigh+1):
                    lists.append(i)
                result.append(lists)
                #低位指针移动 继续找下一组
                plow=plow+1
            elif cur<sum:
                #如果当前窗口内的值之和小于sum，那么右边窗口右移一下
                phigh=phigh+1
            else:
                #如果当前窗口内的值之和大于sum，那么左边窗口右移一下
                plow=plow+1
        return result


if __name__ == '__main__':
    s=9
    a=Solution()
    result = a.FindContinuousSequence(s)
    print(result)