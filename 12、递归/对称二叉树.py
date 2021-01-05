# -*- coding: utf-8 -*-
"""
@File    :   对称二叉树.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/5 15:10    1.0         None
# 给定一个二叉树，检查它是否是镜像对称的。
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#      1
#    / \
#   2   2
#    \   \
#    3    3
#
#  进阶：
#  你可以运用递归和迭代两种方法解决这个问题吗？
#  Related Topics 树 深度优先搜索 广度优先搜索
"""
__author__ = 'haochen214934'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q=[root]
        while q:
            flag=[]
            value=[]
            for i in q:
                if i:
                    value.append(i.val)
                    flag.append(i.left)
                    flag.append(i.right)
                else:
                    value.append(None)
            mid=len(value)//2
            for j in range(mid):
                if value[j]!=value[len(value)-j-1]:
                    return False
            q=flag
        return True

    #递归
    def isSymmetric1(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.checkTwoTree(root.left,root.right)

    def checkTwoTree(self,leftTree, rightTree):#判断左右指数是否对称
        if not leftTree and not rightTree:
            return True
        if not leftTree and rightTree:
            return False
        if leftTree and not rightTree:
            return False
        if leftTree.val!=rightTree.val:
            return False
        left=self.checkTwoTree(leftTree.left,rightTree.right)
        right=self.checkTwoTree(leftTree.right,rightTree.left)
        return left and right

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
    flag = s.isSymmetric1(rightTree7)
    print(flag)