# -*- coding: utf-8 -*-
"""
@File    :   中序遍历.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/9 14:54    1.0         None
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    若二叉树为空，为空操作；否则（1）中序遍历左子树；（2）访问根结点；（3）中序遍历右子树。
    '''
    def inorderTraversal(self, root: TreeNode) -> List[int]:#递归
        if root.left is not None:
            self.inorderTraversal(root.left)
        if root.val is not None:
            print(root.val, end=" ")
        if root.right is not None:
            self.inorderTraversal(root.right)

    def inorderTraversal1(self, root: TreeNode) -> List[int]:#迭代
        flag=[]
        while flag or root:
            while root:
                flag.append(root)
                root=root.left
            root=flag.pop()
            root=root.right


if __name__ == '__main__':
    # 构造二叉树
    rightTree1=TreeNode(2)
    rightTree1.right=TreeNode(5)
    rightTree1.left=TreeNode(4)

    rightTree2=TreeNode(3)
    rightTree2.left=TreeNode(6)
    rightTree2.right=TreeNode(7)

    rightTree3=TreeNode(1)
    rightTree3.left=rightTree1
    rightTree3.right=rightTree2

    s=Solution()
    s.inorderTraversal1(rightTree3)