# 给定一棵二叉搜索树，请找出其中第k大的节点。
#
#  示例 1:
#  输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4
#
#  示例 2:
#  输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4
#
#  限制：
#
#  1 ≤ k ≤ 二叉搜索树元素个数

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        lists =[]
        self.check(root,k,lists)
        return lists[-k]

    def check(self,root:TreeNode,k: int,lists):
        if root.left:
            self.check(root.left,k,lists)
        if root.val:
            lists.append(root.val)
        if root.right:
            self.check(root.right,k,lists)


if __name__ == '__main__':
    l = TreeNode(2)
    l.left = TreeNode(1)


    l1 = TreeNode(3)
    l1.left = l
    l1.right = TreeNode(4)


    l2 = TreeNode(5)
    l2.left = l1
    l2.right = TreeNode(6)

    s=Solution()
    f=s.kthLargest(l2,3)
    print(f)