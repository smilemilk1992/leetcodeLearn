# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。”
#
#  例如，给定如下二叉搜索树: root = [6,2,8,0,4,7,9,null,null,3,5]
#
#  示例 1:
#  输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
#
#
#  示例 2:
#  输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
#
#  说明:
#
#  所有节点的值都是唯一的。
#  p、q 为不同节点且均存在于给定的二叉搜索树中。
#
#
#  注意：本题与主站 235 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a
# -binary-search-tree/
#  Related Topics 树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root ==p or root==q or root is None:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and not right:
            return left#左子树上能找到，但是右子树上找不到，此时就应当直接返回左子树的查找结果
        elif not left:
            return right#右子树上能找到，但是左子树上找不到，此时就应当直接返回右子树的查找结果
        else:
            #//左右子树上均能找到，说明此时的p结点和q结点分居root结点两侧，此时就应当直接返回root结点
            return root