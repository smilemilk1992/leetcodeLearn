# -*- coding: utf-8 -*-
"""
@File    :   二叉树的最近公共祖先.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/5 17:28    1.0         None
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。”
#
#  例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]
#
#  示例 1:
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
#  示例 2:
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#
#  说明:
#  所有节点的值都是唯一的。
#  p、q 为不同节点且均存在于给定的二叉树中。
#
#  Related Topics 树
"""
__author__ = 'haochen214934'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #递归
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


if __name__ == '__main__':
    rightTree1 = TreeNode(4)

    rightTree2 = TreeNode(5)
    rightTree2.left = TreeNode(8)
    rightTree2.right = TreeNode(9)

    rightTree3 = TreeNode(5)

    rightTree4 = TreeNode(4)
    rightTree4.left = TreeNode(9)
    rightTree4.right = TreeNode(8)

    rightTree5 = TreeNode(3)
    rightTree5.left = rightTree1
    rightTree5.right = rightTree2

    rightTree6 = TreeNode(3)
    rightTree6.left = rightTree3
    rightTree6.right = rightTree4

    rightTree7 = TreeNode(2)
    rightTree7.left = rightTree5
    rightTree7.right = rightTree6

    s = Solution()
    flag = s.lowestCommonAncestor(rightTree7,3,8)
    print(flag)