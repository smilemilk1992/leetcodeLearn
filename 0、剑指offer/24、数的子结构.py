# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
#
#  B是A的子结构， 即 A中有出现和B相同的结构和节点值。
#
#  例如:
# 给定的树 A:
#
#  3
#  / \
#  4 5
#  / \
#  1 2
# 给定的树 B：
#
#  4
#  /
#  1
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
#
#  示例 1：
#  输入：A = [1,2,3], B = [3,1]
# 输出：false
#
#
#  示例 2：
#  输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true
#
#  限制：
#
#  0 <= 节点个数 <= 10000
#  Related Topics 树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def subStructureCheck(self, A, B):
        if B is None:
            return True
        if A is None or (A.val != B.val):
            return False
        return self.subStructureCheck(A.left, B.left) and self.subStructureCheck(A.right, B.right)

    def isSubStructure(self, A, B):
        result = False
        if A and B:
            if A.val == B.val:
                result = self.subStructureCheck(A, B)
            if not result:
                result = self.isSubStructure(A.left, B)
            if not result:
                result = self.isSubStructure(A.right, B)

        return result
