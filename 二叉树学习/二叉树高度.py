# -*- coding: utf-8 -*-
"""
@File    :   二叉树高度.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/10 9:27    1.0         None
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    #迭代
    def height(self, root: TreeNode) -> List[int]:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is not None and root.right is None:
            high=1+self.height(root.left)
        elif root.left is  None and root.right is not None:
            high=1+self.height(root.right)
        else:
            high=1+max(self.height(root.left),self.height(root.right)) #都不为空的情况
        return high

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
    h = s.height(rightTree3)
    print(h)