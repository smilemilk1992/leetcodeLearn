# -*- coding: utf-8 -*-
"""
@File    :   q108将有序数组转为高度平衡二叉树.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/30 11:10    1.0         None
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #中序遍历
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left,right):
            if left>right:
                return None
            p=(left+right)//1
            root=TreeNode(nums[p])
            root.left=helper(left,p-1)
            root.right=helper(p+1,right)
            return root

        return helper(0,len(nums)-1)

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
    s = Solution()
    nums=[1,2,3,4,5,6,7,8]
    flag=s.sortedArrayToBST(nums)
    s.inorderTraversal1(flag)
