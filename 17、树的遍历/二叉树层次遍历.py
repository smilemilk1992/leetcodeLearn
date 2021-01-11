# -*- coding: utf-8 -*-
"""
@File    :   二叉树层次遍历.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/11 15:40    1.0         None
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#  示例：
# 二叉树：[3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  返回其层序遍历结果：
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  Related Topics 树 广度优先搜索
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res=[]
        flag=[root]
        while flag:
            cur=[]
            fg=[]
            for f in flag:
                fg.append(f.val)
                if f.left:
                    cur.append(f.left)
                if f.right:
                    cur.append(f.right)
            res.append(fg)
            flag=cur
        return res



if __name__ == '__main__':
    rightTree1 = TreeNode(2)
    rightTree1.right = TreeNode(5)
    rightTree1.left = TreeNode(4)

    rightTree2 = TreeNode(3)
    rightTree2.left = TreeNode(6)
    rightTree2.right = TreeNode(7)

    rightTree3 = TreeNode(1)
    rightTree3.left = rightTree1
    rightTree3.right = rightTree2

    s=Solution()
    f=s.levelOrder(rightTree3)
    print(f)