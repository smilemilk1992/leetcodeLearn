# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
#
#  示例 1:
#  给定二叉树 [3,9,20,null,null,15,7]
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回 true 。
#
# 示例 2:
#  给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#         1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#
#  返回 false 。
#
#  限制：
#  1 <= 树的结点个数 <= 10000
#
#
#  注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/
#  Related Topics 树 深度优先搜索

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        left=self.check(root.left)
        right=self.check(root.right)
        if abs(right-left)>1:
            return False
        return True

    def check(self,root):#二叉树深度
        res = 0
        if root is None:
            return res
        head = [root]
        while head:
            c = []
            for i in head:
                if i.left:
                    c.append(i.left)
                if i.right:
                    c.append(i.right)
            res = res + 1
            head = c
        return res



