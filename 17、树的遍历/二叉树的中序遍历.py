# -*- coding: utf-8 -*-
"""
@File    :   二叉树的中序遍历.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/11 15:23    1.0         None
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
#
#  示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
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
# 输出：[2,1]
#
#  示例 5：
# 输入：root = [1,null,2]
# 输出：[1,2]
#
#  提示：
#  树中节点数目在范围 [0, 100] 内
#  -100 <= Node.val <= 100
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树 哈希表
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        self.result(root,res)
        return res
    def result(self,root,res):
        if root.left is not None:
            self.result(root.left,res)
        if root.val is not None:
            res.append(root.val)
        if root.right is not None:
            self.result(root.right,res)

    #迭代
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        res=[]
        while root or res:
            while root:
                res.append(root)
                root=root.left
            root=res.pop()
            root=root.right

if __name__ == '__main__':
    node2=TreeNode(2)
    node2.left=TreeNode(3)

    node1=TreeNode(1)
    node1.right=node2
    s=Solution()
    f=s.inorderTraversal1(node1)
    print(f)