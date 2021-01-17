#写程序判断一颗二叉树是不是完全对称二叉树

#写程序判断两颗二叉树是不是相同


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #判断是否是完全对称二叉树
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.checkSymmetric(root.left,root.right)

    def checkSymmetric(self,leftTree: TreeNode,rightTree: TreeNode):
        if leftTree is None and rightTree is None:
            return True
        if leftTree is not None and rightTree is None:
            return False
        if leftTree is None and rightTree is not None:
            return False
        if leftTree.val!=rightTree.val:
            return False
        left=self.checkSymmetric(leftTree.left,rightTree.right)
        right=self.checkSymmetric(leftTree.right,rightTree.left)
        return left and right

    #判断两个二叉树是不是相等
    def sameTree(self,root1: TreeNode,root2: TreeNode) -> bool:
        return self.checkSameTree(root1,root2)

    def checkSameTree(self,root1: TreeNode,root2: TreeNode):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root1 is not None and root2 is None:
            return False
        if root1.val!=root2.val:
            return False
        left=self.checkSameTree(root1.left,root2.left)
        right =self.checkSameTree(root1.right,root2.right)
        return left and right

if __name__ == '__main__':
    s=Solution()

    rightTree1 = TreeNode(4)
    rightTree2 = TreeNode(6)
    rightTree2.left = TreeNode(3)
    rightTree2.right = TreeNode(7)
    rightTree3 = TreeNode(5)
    rightTree3.left = rightTree1
    rightTree3.right = rightTree2

    rightTree11 = TreeNode(4)
    rightTree22 = TreeNode(6)
    rightTree22.left = TreeNode(3)
    rightTree22.right = TreeNode(7)
    rightTree33 = TreeNode(5)
    rightTree33.left = rightTree11
    rightTree33.right = rightTree22

    f1=s.sameTree(rightTree3,rightTree33)
    print(f1)