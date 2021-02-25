# -*- coding: utf-8 -*-
"""
@File    :   24、归并排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/25 14:31    1.0         None
"""
__author__ = 'haochen214934'
def merge(left,right):
    l=0
    r=0
    new_list=[]
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            new_list.append(left[l])
            l=l+1
        else:
            new_list.append(right[r])
            r=r+1
    new_list=new_list+left[l:]
    new_list=new_list+right[r:]
    return new_list

def merge_sort(nums):
    if(len(nums)<=1):
        return nums
    mid=len(nums)//2
    left=merge_sort(nums[:mid])
    right=merge_sort(nums[mid:])
    return merge(left,right)

if __name__ == '__main__':
    nums=[1,3,2,5,4,7,6]
    print(merge_sort(nums))