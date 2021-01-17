# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数
# 值排序之后中间两个数的平均值。
#
#  例如，
#
#  [2,3,4] 的中位数是 3
#
#  [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
#  设计一个支持以下两种操作的数据结构：
#
#
#  void addNum(int num) - 从数据流中添加一个整数到数据结构中。
#  double findMedian() - 返回目前所有元素的中位数。
#
#
#  示例 1：
#
#  输入：
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
# 输出：[null,null,null,1.50000,null,2.00000]
#
#
#  示例 2：
#
#  输入：
# ["MedianFinder","addNum","findMedian","addNum","findMedian"]
# [[],[2],[],[3],[]]
# 输出：[null,null,2.00000,null,2.50000]
#
#
#
#  限制：
#
#
#  最多会对 addNum、findMedian 进行 50000 次调用。
#
#
#  注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-strea
# m/
#  Related Topics 堆 设计

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lists=[]


    def addNum(self, num: int) -> None:
        self.lists.append(num)


    def findMedian(self) -> float:
        length=len(self.lists)
        low=0
        high=length-1
        self.lists.sort()
        mid=(low+high)//2
        if length%2==1:
            return self.lists[mid]
        else:
            return (self.lists[mid]+self.lists[mid+1])/2.00000



if __name__ == '__main__':
    s=MedianFinder()
    s.addNum(6)
    print(s.findMedian())
    s.addNum(10)
    print(s.findMedian())
    s.addNum(2)
    print(s.findMedian())
    s.addNum(5)
    print(s.findMedian())
    s.addNum(0)
    print(s.findMedian())
    s.addNum(6)
    print(s.findMedian())
    s.addNum(3)
    print(s.findMedian())
    s.addNum(1)
    print(s.findMedian())
    s.addNum(0)
    print(s.findMedian())
    s.addNum(0)
    print(s.findMedian())

