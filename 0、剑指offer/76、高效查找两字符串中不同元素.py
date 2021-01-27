# -*- coding: utf-8 -*-
"""
@File    :   76、高效查找两字符串中不同元素.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/27 15:48    1.0         None
"""
__author__ = 'haochen214934'

class Solution:
    def find(self, list1,list2):

        left=0
        right=min(len(list1),len(list2))-1

        while left<right:
            mid=(left+right)//2
            if list1[left:mid]==list2[left:mid]:
                left=mid+1
            print(left, right, mid)
            # if mid==left:
            #     left=left+1


        if len(list1)>len(list2):
            return list1[left]
        else:
            return list2[left]




if __name__ == '__main__':
    s=Solution()
    list1=["a","c","d","e","f","g"]
    list2=["a","b","c","d","e","f","g"]
    f=s.find(list1,list2)
    print(f)

'''
存储：
    mysql
    活动id,用户id,好友id,砍价钱数,请求时间
    
    redis缓存 保证幂等性
    key：活动id+用户id+好友id
    value:时间戳
    
    redis 分布式锁
    根据 活动id+用户id 设置锁 同一个用户id发过来的请求都会有序请求接口
    
    redis INCR自增
     返回 11-num>0:
     :return 11-num
     else:
     :return 谢谢您的帮助
    
    
'''