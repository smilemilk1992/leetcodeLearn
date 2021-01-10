# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#
#
#
#  例如，给出
#
#  后序遍历 laterorder = [9，15，7，20，3]
# 中序遍历 inorder = [9,3,15,20,7]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
#  限制：
#
#  0 <= 节点个数 <= 5000
#
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/
#  Related Topics 树 递归
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, laterorder: List[int], inorder: List[int]) -> TreeNode:
        if len(laterorder) == 0:
            return None
        if len(laterorder) == 1:
            return TreeNode(laterorder[0])
        root_val = laterorder[-1]
        idx = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(laterorder[:idx], inorder[:idx])
        root.right = self.buildTree(laterorder[idx :-1], inorder[idx + 1:])
        return root

if __name__ == '__main__':
    s=Solution()
    laterorder = [9,15,7,20,3] #后序遍历
    inorder = [9, 3, 15, 20, 7] #中序遍历
    s.buildTree(laterorder,inorder)