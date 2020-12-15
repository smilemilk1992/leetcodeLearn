# -*- coding: utf-8 -*-
"""
@File    :   q98验证二叉搜索树.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/11 10:41    1.0         None

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
#  假设一个二叉搜索树具有如下特征：
#
#
#  节点的左子树只包含小于当前节点的数。
#  节点的右子树只包含大于当前节点的数。
#  所有左子树和右子树自身必须也是二叉搜索树。
#
#
#  示例 1:
#
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#
#
#  示例 2:
#
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        return self.checkTwoTree(root)

    def checkTwoTree(self,root,lower = float('-inf'), upper = float('inf')):
        if not root:
            return True
        val=root.val
        if val<=lower or val>=upper:
            return False
        if not self.checkTwoTree(root.left,lower,val):#因为左子树里所有节点的值均小于它的根节点的值
            return False
        if not self.checkTwoTree(root.right,val,upper):#因为右子树里所有节点的值均大于它的根节点的值
            return False
        return True

    #方法二 中序遍历 序列一定是升序
    '''
    基于方法一中提及的性质，我们可以进一步知道二叉搜索树「中序遍历」得到的值构成的序列一定是升序的，
    这启示我们在中序遍历的时候实时检查当前节点的值是否大于前一个中序遍历到的节点的值即可。
    如果均大于说明这个序列是升序的，整棵树是二叉搜索树，否则不是，下面的代码我们使用栈来模拟中序遍历的过程。
    '''
    def isValidBST1(self, root: TreeNode) -> bool:
        stack,inorder=[],float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val<=inorder:
                return False
            # print(root.val)
            inorder=root.val
            root=root.right

        return True



    def preorderTraversal(self, root: TreeNode) -> List[int]:#递归
        if root.val is not None:
            print(root.val, end=" ")
        if root.left is not None:
            self.preorderTraversal(root.left)
        if root.right is not None:
            self.preorderTraversal(root.right)

if __name__ == '__main__':
    # 构造二叉树

    # rightTree3 = TreeNode(0)
    # rightTree3.left = TreeNode(-1)
    #
    #
    rightTree1 = TreeNode(4)

    rightTree2 = TreeNode(6)
    rightTree2.left=TreeNode(3)
    rightTree2.right = TreeNode(7)

    rightTree3 = TreeNode(5)
    rightTree3.left = rightTree1
    rightTree3.right = rightTree2

    s=Solution()
    flag=s.isValidBST1(rightTree3)
    print(flag)