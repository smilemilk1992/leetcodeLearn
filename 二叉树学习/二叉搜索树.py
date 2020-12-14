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
    def __init__(self, val=0, left=None, right=None,parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def getparent(self,root: TreeNode, treenode: TreeNode):#获取父节点
        if root.val==treenode.val:#根节点相同
            return None
        cur=root
        while cur:
            if cur.left.val==treenode.val or cur.right.val==treenode.val:
                return cur
            elif treenode.val<cur.val:
                cur=cur.left
            else:
                cur=cur.right
        return None


    def insertBST(self, root: TreeNode, value: int ) -> bool:#二叉树插入
        node=TreeNode(value)
        if not root:
            return node
        cur=root
        while cur:
            if value==cur.val:
                break
            elif value>cur.val:
                if cur.right is None:
                    cur.right=node
                else:
                    cur=cur.right
            else:
                if cur.left is None:
                    cur.left=node
                else:
                    cur=cur.left
        return root

    def insertBST1(self, root: TreeNode, value: int) -> bool:  # 二叉树插入
        # node是空
        if not root:#插入
            # 只是创建节点，但是没有连接起来  空树，递归不需要特殊出来
            root = TreeNode(value)
        # 12 < 17 往左走
        elif value < root.val:
            # 这是父亲连着左孩子   --这是左孩子
            root.left = self.insertBST1(root.left, value)
            # 这是左孩子的父亲是 --这是父亲
            root.left.parent = root
            # 这是右孩子
        elif value > root.val:
            root.right = self.insertBST1(root.right, value)
            # 右孩子连着父亲
            root.right.parent = root
        return root

    def queryBST(self, root: TreeNode,value: int ) -> bool:#二叉树查询-递归
        if not root:
            return False
        def check(root,value):
            if not root:
                return False
            if root:
                if value==root.val:
                    return True
            a=check(root.left,value)#先查询左边
            if a:
                return a
            b=check(root.right,value)#再查询右边
            if b:
                return b
            return False
        return check(root,value)

    def queryBST1(self, root: TreeNode,value: int ) -> bool:#二叉树查询-递归
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

    def queryBST2(self, root: TreeNode,value: int ) -> bool:#二叉树查询-递归循环
        if not root:
            return False
        while root:
            if value==root.val:
                return True
            elif value>root.val:
                root=root.right
            else:
                root=root.left
        return False

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
    # flag=s.queryBST2(rightTree3,40)
    flag = s.insertBST1(rightTree3,8)
    #
    # dell= s.delBST(rightTree3,10)
    s.inorderTraversal1(flag)
