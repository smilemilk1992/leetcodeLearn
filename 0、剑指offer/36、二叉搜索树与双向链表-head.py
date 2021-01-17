# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
#
#  为了让您更好地理解问题，以下面的二叉搜索树为例：
#
#  我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是
# 第一个节点。
#
#  下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
#
#  特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
#
#  注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-
# to-sorted-doubly-linked-list/
#
#  注意：此题对比原题有改动。
#  Related Topics 分治算法

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # 如果节点为空，直接返回
        def build(root):
            if not root.left and not root.right:
                return root, root
            # 如果节点没有左右子树，那么它的双向链表仅包含它自身。递归终止（这一句可以删去）
            new_head, new_end = root, root
            # 否则，双向链表不仅包含当前节点。
            # 使用两个变量记录现在的头尾，然后
            # 准备把左子树链表或右子树链表拼接上去
            if root.left:
                # 如果有左子树，那么把对应链表拼在当前节点左边
                head, end = build(root.left)  # 自我调用，把左子树转成双向链表，返回其头尾
                end.right = root  # 把左子树的尾指向当前节点
                root.left = end  # 把当前节点的头指向左子树的尾
                new_head = head  # 最终得到的链表的头，是左子树链表的头
            if root.right:
                # 如果有右子树，把它拼在当前节点右边
                # 操作完全类似
                head, end = build(root.right)
                root.right = head
                head.left = root
                new_end = end
            # 返回得到的链表的头尾
            return new_head, new_end

        # 将根节点输入上述函数得到双向链表
        head, end = build(root)
        # 依题意，把双向链表首尾链接
        head.left = end
        end.right = head
        return head
