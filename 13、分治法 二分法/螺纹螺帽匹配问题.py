#给你一堆螺母和螺帽，每个螺母都有一个相对应的螺帽，但是他们之间的对应关系已经打乱。你可以比较螺母和螺帽的大小关系，但是你无法比较螺母和螺母的大小关系，你也无法比较螺帽和螺帽的大小关系。时间复杂度nlogn。

#https://blog.csdn.net/shulixu/article/details/97612890

#https://blog.csdn.net/qq_42791805/article/details/102398392?utm_medium=distribute.pc_relevant.none-task-blog-searchFromBaidu-12.not_use_machine_learn_pai&depth_1-utm_source=distribute.pc_relevant.none-task-blog-searchFromBaidu-12.not_use_machine_learn_pai
'''
    首先选择螺丝中的一个元素作为pivot，用螺丝把螺母分区，每次分区得到三个结果，
    A1，完全匹配的一对
    A2，比螺丝小的螺母
    A3，比螺丝大的螺母
    将1中的螺母取出，用它对螺丝进行分区，可以得到
    B1. 比螺母小的螺丝
    B2. 比螺母大的螺丝
    A2跟B1一一对应，A3跟B2一一对应，对(A2,B1)和(A3,B2)分别执行上述的算法，直至完全匹配。
    a=[4,5,2,6,1,7,8,9,3]
    b=[6,2,1,8,9,7,4,5,3]
'''

class Solution:
    def __init__(self):
        self.n=1
    def match(self,a,b):
        self.sort(a,b,0,len(a)-1)
        print(a)
        print(b)

    def sort(self,a,b,left,right):
        if left>=right:
            return
        temp=a[left] #用a来区分b
        i = left
        j = right
        while i<j:
            while i<j and b[i]<temp:
                i=i+1
            while i<j and b[j]>temp:
                j=j-1
            b[i],b[j]=b[j],b[i]
        b[i],b[left]=b[left],b[i]
        print("滴{}次操作 b:{}".format(self.n,b))
        temp=b[left+1] #用b来区分a
        i = left + 1
        j = right
        while i<j:
            while i<j and a[i]<temp:
                i=i+1
            while i<j and a[j]>temp:
                j=j-1
            a[i], a[j] = a[j], a[i]
        a[left+1],a[i]=a[i],a[left+1]
        print("滴{}次操作 a:{}".format(self.n, a))
        self.n=self.n+1
        self.sort(a,b,left+2,i)
        self.sort(a,b,i+1,right)


if __name__ == '__main__':
    s=Solution()
    a=[4,5,2,6,1,7,8,9,3]
    b=[6,2,1,8,9,7,4,5,3]
    s.match(a,b)