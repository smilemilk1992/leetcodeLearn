# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
#
#
#
#  例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回：
#
#  [3,9,20,15,7]
#
#
#
#
#  提示：
#
#
#  节点总数 <= 1000
#
#  Related Topics 树 广度优先搜索
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        flag=[root]
        res=[]
        while flag:
            c=[]
            for i in flag:
                if i is not None:
                    res.append(i.val)
                    c.append(i.left)
                    c.append(i.right)
            flag=c
        return res



