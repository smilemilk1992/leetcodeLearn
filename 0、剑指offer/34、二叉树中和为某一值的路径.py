# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
#  示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#
#
#  返回:
#
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
#  提示：
#  节点总数 <= 10000
#
#  注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/
#  Related Topics 树 深度优先搜索
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path,flag = [], [],0

        self.check(root,sum,res,path,flag)
        return res

    def check(self,root,sum,res,path,flag):
        if not root:
            return
        path.append(root.val)
        flag=flag+root.val
        if flag==sum and not root.left and not root.right:
            res.append(list(path))
        self.check(root.left,sum,res,path,flag)
        self.check(root.right,sum,res,path,flag)
        if path:
            path.pop()



if __name__ == '__main__':
    s=Solution()
    l=TreeNode(11)
    l.left=TreeNode(7)
    l.right=TreeNode(2)

    l1=TreeNode(4)
    l1.left=TreeNode(5)
    l1.right=TreeNode(1)

    l2=TreeNode(4)
    l2.left=l

    l3=TreeNode(8)
    l3.left=TreeNode(13)
    l3.right=l1

    l4=TreeNode(5)
    l4.left=l2
    l4.right=l3

    f=s.pathSum(l4,22)
    print(f)