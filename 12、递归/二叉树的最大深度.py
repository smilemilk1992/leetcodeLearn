# -*- coding: utf-8 -*-
"""
@File    :   二叉树的最大深度.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/5 15:49    1.0         None
# 给定一个二叉树，找出其最大深度。
#
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回它的最大深度 3 。
#  Related Topics 树 深度优先搜索 递归
"""
__author__ = 'haochen214934'

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #深度优先
    def maxDepth(self, root: TreeNode) -> int:
        flag=[root]
        res=[]
        while flag:
            temp=[]
            r=[]
            for q in flag:
                if q:
                    r.append(q.val)
                    temp.append(q.left)
                    temp.append(q.right)
            if r:
                res.append(r)
            flag=temp
        return len(res)

    #递归
    def maxDepth1(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left  and not root.right:
            high= 1+self.maxDepth(root.left)
        if not root.left and root.right:
            high= 1+self.maxDepth(root.right)
        if root.left and root.right:
            high= 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        return high



if __name__ == '__main__':
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

    s = Solution()
    flag = s.maxDepth1(rightTree7)
    print(flag)