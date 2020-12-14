# -*- coding: utf-8 -*-
"""
@File    :   q701_二叉搜索树中的插入操作.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/11 10:41    1.0         None
# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值
# 都不同。
#
#  注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。
#  示例 1：
# 输入：root = [4,2,7,1,3], val = 5
# 输出：[4,2,7,1,3,5]
# 解释：另一个满足题目要求可以通过的树是：
#
#  示例 2：
# 输入：root = [40,20,60,10,30,50,70], val = 25
# 输出：[40,20,60,10,30,50,70,null,null,25]
#
#
#  示例 3：
# 输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# 输出：[4,2,7,1,3,5]
#
#  提示：
#  给定的树上的节点数介于 0 和 10^4 之间
#  每个节点都有一个唯一整数值，取值范围从 0 到 10^8
#  -10^8 <= val <= 10^8
#  新值和原始二叉搜索树中的任意节点值都不同
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node=TreeNode(val)
        if not root:
            return node
        cur=root
        while cur:
            if val==cur.val:
                break
            elif val<cur.val:
                if cur.left is None:
                    cur.left=node
                else:
                    cur=cur.left
            else:
                if cur.right is None:
                    cur.right=node
                else:
                    cur=cur.right
        return root


    def inorderTraversal1(self, root: TreeNode) -> List[int]:  # 迭代 中序遍历
        flag = []
        while flag or root:
            while root:
                flag.append(root)
                root = root.left
            root = flag.pop()
            print(root.val)
            root = root.right

if __name__ == '__main__':
    # 构造二叉树
    rightTree = TreeNode(1)

    rightTree1 = TreeNode(6)
    rightTree1.left = TreeNode(4)
    rightTree1.right = TreeNode(7)

    rightTree2 = TreeNode(14)
    rightTree2.left = TreeNode(11)

    rightTree3 = TreeNode(10)
    rightTree3.right = rightTree2

    rightTree4 = TreeNode(3)
    rightTree4.left = rightTree
    rightTree4.right = rightTree1

    rightTree5 = TreeNode(8)
    rightTree5.left = rightTree4
    rightTree5.right = rightTree3

    s = Solution()
    sss = s.insertIntoBST(rightTree5, 15)
    s.inorderTraversal1(sss)