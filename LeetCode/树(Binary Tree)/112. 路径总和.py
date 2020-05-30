"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
from functools import reduce


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        思路：dfs
        1. 遇到return True，反之False
        2. 利用reduce求数组和
        """
        def findPath(root, arr):
            if not root:
                return False
            if not root.left and not root.right:
                arr.append(root.val)
                if reduce(lambda x, y: x + y, arr) == sum:
                    return True
                arr.pop()
                return False
            return findPath(root.left, arr + [root.val]) or findPath(root.right, arr + [root.val])

        return findPath(root, [])