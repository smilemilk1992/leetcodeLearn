# -*- coding: utf-8 -*-
"""
@File    :   平衡二叉树.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/11 16:26    1.0         None
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#  本题中，一棵高度平衡二叉树定义为：
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
#
#  示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true

#  示例 2：
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#  示例 3：
# 输入：root = []
# 输出：true
#
#  提示：
#
#  树中的节点数在范围 [0, 5000] 内
#  -104 <= Node.val <= 104
#  Related Topics 树 深度优先搜索 递归
"""
__author__ = 'haochen214934'

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self,root):
        if root is None:
            return 0
        else:
            l=self.height(root.left)
            r=self.height(root.right)
            return max(l,r)+1



    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if abs(self.height(root.left)-self.height(root.right))>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

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
    s.isBalanced(rightTree3)
