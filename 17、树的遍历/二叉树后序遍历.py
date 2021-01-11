# -*- coding: utf-8 -*-
"""
@File    :   二叉树后序遍历.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/11 16:03    1.0         None
# 给定一个二叉树，返回它的 后序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [3,2,1]
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        if not root:
            return res
        self.result(root,res)
        return res

    def result(self,root,res):
        if root.left:
            self.result(root.left,res)
        if root.right:
            self.result(root.right,res)
        if root.val:
            res.append(root.val)


# 迭代
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        res = []
        stack =[]
        if not root:
            return res
        stack.append(root)
        while stack:
            temp=stack.pop()
            res.insert(0,temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
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
    s = Solution()
    f=s.postorderTraversal1(rightTree3)
    print(f)