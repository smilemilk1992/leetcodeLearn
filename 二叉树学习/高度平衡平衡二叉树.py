# -*- coding: utf-8 -*-
"""
@File    :   高度平衡平衡二叉树.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/9 15:10    1.0         None
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#  本题中，一棵高度平衡二叉树定义为：
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
#
#  示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#
#  示例 2：
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#
#  示例 3：
# 输入：root = []
# 输出：true

#  提示：
#  树中的节点数在范围 [0, 5000] 内
#  -104 <= Node.val <= 104
#
#  Related Topics 树 深度优先搜索
"""
__author__ = 'haochen214934'


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def height(self,root: TreeNode)-> int:
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

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        lhigh = 1 + self.height(root.left)
        rhigh = 1 + self.height(root.right)
        if abs(lhigh - rhigh) > 1:
            return False
        re_l = self.isBalanced(root.left)
        re_r = self.isBalanced(root.right)
        return re_l and re_r

if __name__ == '__main__':
    # 构造二叉树
    rightTree1=TreeNode(3)
    rightTree1.left=TreeNode(4)
    rightTree1.right = None

    rightTree2 = TreeNode(3)
    rightTree2.left = None
    rightTree2.right = TreeNode(4)

    rightTree3 = TreeNode(2)
    rightTree3.left = rightTree1
    rightTree3.right = None

    rightTree4 = TreeNode(2)
    rightTree4.left = None
    rightTree4.right = rightTree2

    rightTree5=TreeNode(1)
    rightTree5.left=rightTree3
    rightTree5.right=rightTree4


    s=Solution()
    flag=s.isBalanced(rightTree5)
    print(flag)