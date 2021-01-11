# -*- coding: utf-8 -*-
"""
@File    :   二叉树的前序遍历.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/11 15:56    1.0         None
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
#
#  示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
#
#  示例 2：
# 输入：root = []
# 输出：[]
#
#  示例 3：
# 输入：root = [1]
# 输出：[1]
#
#  示例 4：
# 输入：root = [1,2]
# 输出：[1,2]
#
#  示例 5：
# 输入：root = [1,null,2]
# 输出：[1,2]
#
#  提示：
#  树中节点数目在范围 [0, 100] 内
#  -100 <= Node.val <= 100
#
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        self.result(root,res)
        return res

    def result(self,root,res):
        if root.val:
            res.append(root.val)
        if root.left:
            self.result(root.left,res)
        if root.right:
            self.result(root.right,res)

    # 迭代
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        res = []
        flag=[]
        while root or res:
            while root:
                flag.append(root.val)
                res.append(root)
                root = root.left
            root = res.pop()
            root = root.right
        return flag

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
    f=s.preorderTraversal1(rightTree3)
    print(f)