class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return 0
        l,r=self.getLeft(root),self.getRight(root)
        return l+r-1

    def getLeft(self,root):
        l1=root
        l=0
        while l1:
            l=l+1
            l1=l1.left
        return l

    def getRight(self,root):
        r=0
        r1=root
        while r1:
            r=r+1
            r1=r1.right
        return r





if __name__ == '__main__':
    # 构造二叉树
    rightTree1 = TreeNode(8)
    rightTree1.right=TreeNode(10)

    rightTree2=TreeNode(7)
    rightTree2.left=TreeNode(9)

    rightTree3=TreeNode(4)
    rightTree3.left=rightTree2
    rightTree3.right=TreeNode(12)

    rightTree4=TreeNode(6)
    rightTree4.right=rightTree1

    rightTree5=TreeNode(5)
    rightTree5.left=rightTree3
    rightTree5.right=rightTree4

    s= Solution()
    f=s.isValidBST(rightTree5)
    print(f)
