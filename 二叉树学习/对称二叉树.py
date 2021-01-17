# -*- coding: utf-8 -*-
"""
@File    :   对称二叉树.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/10 10:15    1.0         None
# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#
#
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#      1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#
#
#  进阶：
#
#  你可以运用递归和迭代两种方法解决这个问题吗？
#  Related Topics 树 深度优先搜索 广度优先搜索
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #判断是否是对称二叉树
    def isSymmetric(self, root: TreeNode) -> bool:#迭代
        if not root:
            return True
        queue=[root]
        while queue:
            flag=[]
            value=[]
            for q in queue:
                if q:
                    value.append(q.val)
                    flag.append(q.left)
                    flag.append(q.right)
                else:
                    value.append(None)
            mid=len(value)//2
            #检查每一层是否是对称的
            for i in range(mid):
                if value[i]!=value[len(value)-i-1]:
                    return False
            queue=flag
        return True


    def isSymmetric1(self, root: TreeNode) -> bool:#递归
        if root is None:
            return False
        return self.checkTwoTree(root.left,root.right)

    def checkTwoTree(self,leftTree, rightTree):#判断左右指数是否对称
        if leftTree is None and rightTree is None:
            return True
        if leftTree is not None and rightTree is None:
            return False
        if leftTree is None and rightTree is not  None:
            return False
        if leftTree.val!=rightTree.val:
            return False
        left=self.checkTwoTree(leftTree.left,rightTree.right)
        right = self.checkTwoTree(leftTree.right,leftTree.left)
        return left and right




    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root.val is not None:
            print(root.val, end=" ")
        if root.left is not None:
            self.preorderTraversal(root.left)
        if root.right is not None:
            self.preorderTraversal(root.right)

if __name__ == '__main__':
    # 构造二叉树
    # rightTree1=TreeNode(2)
    # rightTree1.left=TreeNode(3)
    # rightTree1.right = TreeNode(4)
    # rightTree2 = TreeNode(2)
    # rightTree2.left = TreeNode(4)
    # rightTree2.right = TreeNode(3)
    # rightTree3 = TreeNode(1)
    # rightTree3.left = rightTree1
    # rightTree3.right = rightTree2
    #
    # rightTree1 = TreeNode(2)
    # rightTree1.right = TreeNode(3)
    # rightTree2 = TreeNode(2)
    # rightTree2.right = TreeNode(3)
    # rightTree3 = TreeNode(1)
    # rightTree3.left = rightTree1
    # rightTree3.right = rightTree2

    rightTree1 = TreeNode(4)

    rightTree2 = TreeNode(5)
    rightTree2.left = TreeNode(8)
    rightTree2.right = TreeNode(9)

    rightTree3 = TreeNode(5)

    rightTree4 = TreeNode(4)
    rightTree4.left = TreeNode(9)
    rightTree4.right = TreeNode(8)

    rightTree5 = TreeNode(3)
    rightTree5.left = rightTree1
    rightTree5.right = rightTree2

    rightTree6 = TreeNode(3)
    rightTree6.left = rightTree3
    rightTree6.right = rightTree4

    rightTree7 = TreeNode(2)
    rightTree7.left = rightTree5
    rightTree7.right = rightTree6

    s=Solution()
    flag=s.isSymmetric1(rightTree7)
    print(flag)