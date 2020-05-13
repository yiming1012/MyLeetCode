"""

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
from typing import List
from MockTreeNode import Mock


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        执行用时 :196 ms, 在所有 Python3 提交中击败了59.36%的用户
        内存消耗 :87.7 MB, 在所有 Python3 提交中击败了11.11%的用户
        题意：给定一棵树的先序遍历和中序遍历结果，构造这棵树并返回根节点
        思路：递归
        preorder = [3, 9, 8, 20, 15, 7]
        inorder = [8, 9, 3, 15, 20, 7]
        1. 先序遍历：根节点 -> 左子树 -> 右子树。即根节点为3，在中序遍历列表中的下标为i=2
        2. 中序遍历：左子树-> 根节点 -> 右子树。所以[8,9]为3的左子树的中序遍历结果，[15,20,7]为右子树的中序遍历结果
        3. 此时，中序遍历[8,9]的长度为2，对应的先序遍历列表为[9,8],对应下标即[1:i+1];而[15,20,7]对应的先序遍历列表即为[20,15,7],对应下标即为[i+1:]
        4. 返回条件：先序遍历列表为空，即返回
        """
        if not preorder:
            return
        head = preorder[0]
        i = inorder.index(head)
        head = TreeNode(head)
        head.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        head.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return head


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(Solution().buildTree(preorder, inorder))
