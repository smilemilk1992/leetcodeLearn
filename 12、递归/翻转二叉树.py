# -*- coding: utf-8 -*-
"""
@File    :   翻转二叉树.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/5 16:51    1.0         None
# 翻转一棵二叉树。
#
#  示例：
#
#  输入：
#
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
#  输出：
#
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
#  备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
#
#  谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
"""
__author__ = 'haochen214934'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        else:
            root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
            return root

    #递归
    def invertTree1(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        flag=[root]
        while len(flag):
            node=flag.pop(0)
            node.right,node.left=node.left,node.right
            if node.left:
                flag.append(node.left)
            if node.right:
                flag.append(node.right)
        return root

    def prift(self,root):#层次遍历输出
        flag=[root]
        while flag:
            temp=[]
            res=[]
            for f in flag:
                if f:
                    res.append(f.val)
                    temp.append(f.left)
                    temp.append(f.right)
            print(res)
            flag=temp


if __name__ == '__main__':
    rightTree1 = TreeNode(2)
    rightTree1.left=TreeNode(1)
    rightTree1.right=TreeNode(3)

    rightTree2 = TreeNode(7)
    rightTree2.left = TreeNode(6)
    rightTree2.right = TreeNode(9)

    rightTree3=TreeNode(4)
    rightTree3.left=rightTree1
    rightTree3.right=rightTree2

    s=Solution()
    flag=s.invertTree1(rightTree3)
    s.prift(flag)

