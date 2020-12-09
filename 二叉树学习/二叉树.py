# -*- coding: utf-8 -*-
"""
@File    :   二叉树.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/9 14:58    1.0         None
https://www.jianshu.com/p/9503238394df
"""
__author__ = 'haochen214934'
from graphviz import Digraph
import uuid
from random import sample

# 二叉树类
class BTree(object):

    # 初始化
    def __init__(self, data=None, left=None, right=None):
        self.data = data    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树

    # 先序遍历
    '''
    若二叉树为空，为空操作；否则（1）访问根节点；（2）先序遍历左子树；（3）先序遍历右子树
    '''
    def preorder(self):
        if self.data is not None:
            print(self.data, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    # 中序遍历
    def inorder(self):

        if self.left is not None:
            self.left.inorder()
        if self.data is not None:
            print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder()

    # 后序遍历
    def postorder(self):

        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=' ')

    # 层序遍历
    def levelorder(self):

        # 返回某个节点的左孩子
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None
        # 返回某个节点的右孩子
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None

        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的数据
        if self.data is not None:
            level_order.append([self])

        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 该层的节点
                for node in level_order[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 如果右孩子非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 如果该层非空，则添加该层
                if level:
                    level_order.append(level)

            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].data

        return level_order

    # 二叉树的高度
    def height(self):
        # 空的树高度为0, 只有root节点的树高度为1
        if self.data is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # 二叉树的叶子节点
    def leaves(self):

        if self.data is None:
            return None
        elif self.left is None and self.right is None:
            print(self.data, end=' ')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.right is None and self.left is not None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()



if __name__ == '__main__':
    # 构造二叉树, BOTTOM-UP METHOD
    right_tree = BTree(6)
    right_tree.left = BTree(2)
    right_tree.right = BTree(4)

    left_tree = BTree(5)
    left_tree.left = BTree(1)
    left_tree.right = BTree(3)

    tree = BTree(11)
    tree.left = left_tree
    tree.right = right_tree

    left_tree = BTree(7)
    left_tree.left = BTree(3)
    left_tree.right = BTree(4)

    right_tree = tree  # 增加新的变量
    tree = BTree(18)
    tree.left = left_tree
    tree.right = right_tree

    print('先序遍历为:')
    tree.preorder()
    print()

    print('中序遍历为:')
    tree.inorder()
    print()

    print('后序遍历为:')
    tree.postorder()
    print()

    print('层序遍历为:')
    level_order = tree.levelorder()
    print(level_order)
    print()

    height = tree.height()
    print('树的高度为%s.' % height)

    print('叶子节点为：')
    tree.leaves()
    print()

    # 利用Graphviz进行二叉树的可视化
    # tree.print_tree(save_path='E://BTree.gv', label=True)