# -*- coding: utf-8 -*-
"""
@File    :   层序遍历.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/9 14:54    1.0         None
"""
__author__ = 'haochen214934'

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    若二叉树为空，为空操作；否则从上到下、从左到右按层次进行访问。
    [1, 2, 3, 4, 5, 6, 7]
    其思路就是将二叉树的节点加入队列，出队的同时将其非空左右孩子依次入队，出队到队列为空即完成遍历。
    '''
    def levelorderTraversal(self, root: TreeNode) -> List[int]:
        outList = []
        queue = [root]
        while queue != []:
            outList.append(queue[0].val)
            if queue[0].left != None:
                queue.append(queue[0].left)
            if queue[0].right != None:
                queue.append(queue[0].right)
            queue.pop(0)
        print(outList)

    '''
    若二叉树为空，为空操作；否则从上到下、从左到右按层次进行访问。
    [1, 2, 3, 4, 5, 6, 7]
    其思路就是将二叉树的节点加入队列，出队的同时将其非空左右孩子依次入队，出队到队列为空即完成遍历。(改进版)
    '''
    def levelorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        currentStack = [root]
        outList = []
        while currentStack:
            nextStack = []
            for point in currentStack:
                if point.left:
                    nextStack.append(point.left)
                if point.right:
                    nextStack.append(point.right)
                outList.append(point.val)
            currentStack = nextStack
        print(outList)

    '''
    若二叉树为空，为空操作；否则从上到下、从左到右按层次进行访问。
    [[1],[2,3],[4,5,6,7]]
    其思路就是将二叉树的节点加入队列，出队的同时将其非空左右孩子依次入队，出队到队列为空即完成遍历。
    '''
    def levelorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        currentStack = [root]
        outList = []
        while currentStack:
            nextStack = []
            c=[]
            for point in currentStack:
                if point.left:
                    nextStack.append(point.left)
                if point.right:
                    nextStack.append(point.right)
                c.append(point.val)
            outList.append(c)
            currentStack = nextStack
        print(outList)




    '''
    若二叉树为空，为空操作；否则从上到下、从左到右按层次进行访问。
    [[1],[2,3],[4,5,6,7]]
    其思路就是将二叉树的节点加入队列，出队的同时将其非空左右孩子依次入队，出队到队列为空即完成遍历。
    '''
    def levelorderTraversal3(self, root: TreeNode) -> List[int]:
        outList = []
        queue = [root]
        while queue != []:
            res=[]
            nextQueue = []
            for point in queue: #这里再遍历每一层
                res.append(point.val)
                if point.left != None:
                    nextQueue.append(point.left)
                if point.right != None:
                    nextQueue.append(point.right)
            outList.append(res)
            queue = nextQueue  # 这一步很巧妙，用当前层覆盖上一层
        print(outList)





if __name__ == '__main__':
    # 构造二叉树
    rightTree1=TreeNode(2)
    rightTree1.right=TreeNode(5)
    rightTree1.left=TreeNode(4)

    rightTree2=TreeNode(3)
    rightTree2.left=TreeNode(6)
    rightTree2.right=TreeNode(7)

    rightTree3=TreeNode(1)
    rightTree3.left=rightTree1
    rightTree3.right=rightTree2

    s=Solution()
    s.levelorderTraversal(rightTree3)