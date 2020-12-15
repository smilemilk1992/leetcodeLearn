# -*- coding: utf-8 -*-
"""
@File    :   q450_删除二叉搜索树中的节点.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/11 10:41    1.0         None
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的
# 根节点的引用。
#  一般来说，删除节点可分为两个步骤：
#  首先找到需要删除的节点；
#  如果找到了，删除它。
#  说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
#  示例:
# root = [5,3,6,2,4,null,7]
# key = 3
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# 另一个正确答案是 [5,2,6,null,4,null,7]。
#     5
#    / \
#   2   6
#    \   \
#     4   7
#  Related Topics 树
删除节点主要有三种情况：
节点只存在左子树，那么我们直接用左子树代替根节点即可；
节点只存在右子树，同样地，我们直接用右子树代替根节点；
同时存在左右子树是比较复杂的情况，这是我们重点关注的情况。
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        # 到左子树里搜索
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        # 到右子树里搜索
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # 存在的子树代替根节点
            if not root.left and not root.right:#如果删除的当前左子数或者右子数为空 那么当前值就是左或者右中存在的一个
                root = None
            else:
                temp = root.right
                # 找到右子树的最小（最左）节点
                while temp.left: #1、查询右子数最小左子树
                    temp = temp.left
                root.val = temp.val #2、替换右子数最小左子树值
                # 继续在右子树里递归
                root.right = self.deleteNode(root.right, temp.val)#3、直到删除右子数最小左子树值
        return root

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
    rightTree=TreeNode(1)

    rightTree1 = TreeNode(6)
    rightTree1.left = TreeNode(4)
    rightTree1.right = TreeNode(7)

    rightTree2 = TreeNode(14)
    rightTree2.left=TreeNode(13)

    rightTree3 = TreeNode(10)
    rightTree3.right = rightTree2

    rightTree4 = TreeNode(3)
    rightTree4.left = rightTree
    rightTree4.right = rightTree1


    rightTree5 = TreeNode(8)
    rightTree5.left = rightTree4
    rightTree5.right = rightTree3

    s = Solution()
    sss=s.deleteNode(rightTree5,7)
    s.inorderTraversal1(sss)