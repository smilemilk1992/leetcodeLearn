# -*- coding: utf-8 -*-
"""
@File    :   二叉搜索树.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/11 15:24    1.0         None
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def insertBST(self, root: TreeNode, value: int ) -> bool:#二叉树插入
        if not root:
            return False
        return self.checkTwoTree(root)

    def queryBST(self, root: TreeNode,value: int ) -> bool:#二叉树查询
        if not root:
            return False
        def check(root,value):
            if not root:
                return False
            if root:
                if value==root.val:
                    return True
            a=check(root.left,value)
            if a:
                return a
            b=check(root.right,value)
            if b:
                return b
            return False
        return check(root,value)

    def queryBST1(self, root: TreeNode,value: int ) -> bool:#二叉树查询
        if not root:
            return False
        def check(root,value):#递归
            if not root:
                return False
            if value>root.val:
                return check(root.right,value)
            elif value<root.val:
                return check(root.left,value)
            else:
                return True

        return check(root,value)

    def inorderTraversal1(self, root: TreeNode) -> List[int]:  # 迭代 中序遍历
        flag = []
        while flag or root:
            while root:
                flag.append(root)
                root = root.left
            root = flag.pop()
            print(root.val)
            root = root.right

if __name__ == '__main__':
    # 构造二叉树
    rightTree1 = TreeNode(6)
    rightTree1.left = TreeNode(4)
    rightTree1.right = TreeNode(7)

    rightTree2 = TreeNode(20)
    rightTree2.left=TreeNode(15)
    rightTree2.right = TreeNode(25)

    rightTree3 = TreeNode(10)
    rightTree3.left = rightTree1
    rightTree3.right = rightTree2

    s=Solution()
    flag=s.queryBST1(rightTree3,25)
    print(flag)
