# -*- coding: utf-8 -*-
"""
@File    :   堆排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/9/15 18:43    1.0         None
"""
__author__ = 'haochen214934'

'''
https://blog.csdn.net/qq_34840129/article/details/80638225
https://blog.csdn.net/qq_28063811/article/details/93034625

9	5	8	2	3	4	7	1
对于大顶堆：arr[i] >= arr[2i + 1] && arr[i] >= arr[2i + 2]

1	3	5	4	2	8	9	7
对于小顶堆：arr[i] <= arr[2i + 1] && arr[i] <= arr[2i + 2]

Step 1： 构造初始堆
初始化堆时是对所有的非叶子结点进行筛选
最后一个非终端元素的下标是[n/2]向下取整，所以筛选只需要从第[n/2]向下取整个元素开始，从后往前进行调整。

Step 2：进行堆排序
堆排序是一种选择排序。建立的初始堆为初始的无序区。
排序开始，首先输出堆顶元素（因为它是最值），将堆顶元素和最后一个元素交换，这样，第n个位置（即最后一个位置）作为有序区，前n-1个位置仍是无序区，对无序区进行调整，得到堆之后，再交换堆顶和最后一个元素，这样有序区长度变为2。。。
不断进行此操作，将剩下的元素重新调整为堆，然后输出堆顶元素到有序区。每次交换都导致无序区-1，有序区+1。不断重复此过程直到有序区长度增长为n-1，排序完成。

https://blog.csdn.net/chibangyuxun/article/details/53018294
若想得到升序，则建立大顶堆，若想得到降序，则建立小顶堆
'''
def heap_sort(elems):
    def siftdown(elems, e, begin, end):  # 向下筛选
        i, j = begin, begin * 2 + 1  # j为i的左子结点
        while j < end:
            if j + 1 < end and elems[j] > elems[j + 1]:  # 如果左子结点大于右子结点
                j += 1  # 则将j指向右子结点
            if e < elems[j]:  # j已经指向两个子结点中较小的位置，
                break  # 如果插入元素e小于j位置的值，则为3者中最小的
            elems[i] = elems[j]  # 能执行到这一步的话，说明j位置元素是三者中最小的，则将其上移到父结点位置
            i, j = j, j * 2 + 1  # 更新i为被上移为父结点的原来的j的位置，更新j为更新后i位置的左子结点
        elems[i] = e  # 如果e已经是某个子树3者中最小的元素，则将其赋给这个子树的父结点
        # 或者位置i已经更新到叶结点位置，则将e赋给这个叶结点。
        # print(elems)

    end = len(elems)
    for i in range(end // 2 - 1, -1, -1):  # 若想得到降序，则建立小顶堆
        print(i,elems[i])
        siftdown(elems, elems[i], i, end)


    for i in range((end - 1), 0, -1):  # 进行堆排序.i最后一个值为1，不需要到0 倒叙
        print(elems)
        e = elems[i]  # 将末尾元素赋给e
        elems[i] = elems[0]  # 交换堆顶与最后一个元素
        siftdown(elems, e, 0, i)

    return (elems)


if __name__ == "__main__":
    print(heap_sort([70,60,12,40,30,8,10]))
