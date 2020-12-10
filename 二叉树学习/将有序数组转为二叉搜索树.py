# -*- coding: utf-8 -*-
"""
@File    :   将有序数组转为二叉搜索树.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/10 10:15    1.0         None
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
#  示例:
#
#  给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#  Related Topics 树 深度优先搜索
"""
__author__ = 'haochen214934'

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    '''
    我们知道，二叉搜索树（BST）中序遍历就是升序序列，那么我们可以从这个角度出发，那么问题就转变为从中序遍历的序列中恢复二叉搜索树。
    那么任选一个元素作为根节点，以元素左边的序列构建左子树，右边序列构建右子树。
    但是由于有限制条件，需要转换为高度平衡二叉树，根据前面给出高度平衡二叉树的概念。那么我们考虑选择数组的中间元素作为根节点来代替前面的任意选择一个元素。
    '''

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:#将有序的数组 还原为中序遍历
        if not nums:
            return None
        l = len(nums)
        mid=l // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])#左子树
        root.right = self.sortedArrayToBST(nums[mid + 1:])#右子树
        return root
        return dfs(0, len(nums) - 1)

    def printf(self,head: TreeNode):#中序遍历
        if head.left:
            self.printf(head.left)
        if head:
            print(head.val)
        if head.right:
            self.printf(head.right)



if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    s = Solution()
    l1 = s.sortedArrayToBST(a)
    s.printf(l1)