# -*- coding: utf-8 -*-
"""
@File    :   插入排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/9/15 17:56    1.0         None
"""
__author__ = 'haochen214934'

from typing import List

'''
每步将一个待排序的纪录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。
步骤：
1 从第一个元素开始，该元素可以认为已经被排序
2 取出下一个元素，在已经排序的元素序列中 从后向前扫描
3 如果该元素（已排序）大于新元素，将该元素移到下一位置
4 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5 将新元素插入到该位置后重复步骤2~5

插入排序的适用场景：一个新元素需要插入到一组已经是有序的数组中，或者是一组基本有序的数组排序。
比较性：排序时元素之间需要比较，所以为比较排序
稳定性：从代码我们可以看出只有比较元素大于当前元素，比较元素才会往后移动，所以相同元素是不会改变相对顺序
时间复杂度：插入排序同样需要两次循坏一个一个比较，故时间复杂度也为O(n^2)
空间复杂度：只需要常数个辅助单元，所以空间复杂度也为O(1)
记忆方法：想象成在书架中插书：先找到相应位置，将后面的书往后推，再将书插入
https://blog.csdn.net/zxm317122667/article/details/83344178
'''
class Solution(object):
    def permute(self, nums: List[int]) -> List[int]:
        length=len(nums)
        for i in range(1,length):
            current=nums[i] # 设置当前需要插入的元素
            j = i - 1  # 前一个元素的索引
            while j>=0 and current<=nums[j]: #while==是将第2个元素等于第一个
                nums[j+1]=nums[j] #往后移
                j=j-1 #继续往前找
            nums[j+1]=current #找到最前面就回过头加1 每趟都需要将待插入元素固定到排序位置
        print(nums)


if __name__ == '__main__':
    num = [4,3,2,10,12,1,5,6]
    a=Solution()
    a.permute(num)