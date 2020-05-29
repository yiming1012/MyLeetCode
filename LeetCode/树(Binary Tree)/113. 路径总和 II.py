"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from functools import reduce
from typing import List
from MockTreeNode import Mock


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def findPath(root, arr):
            if not root.left and not root.right:
                if reduce(lambda x, y: x + y, arr) == sum:
                    res.append(arr.copy())
                return
            if root.left:
                findPath(root.left, arr + [root.left.val])
            if root.right:
                findPath(root.right, arr + [root.right.val])

        if not root:
            return []
        findPath(root, [root.val])
        return res

    def pathSum2(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        思路：dfs
        1. 不用每次去判断root.left和root.right是否为空
        2. 当某个节点的左右子节点都为空（叶子节点）时，将该节点添加到数组中，并判断数组和是否为sum
        3. 注意加到数组中的元素需要pop出来
        """
        def findPath(root, arr):
            if not root:
                return
            if not root.left and not root.right:
                arr.append(root.val)
                if reduce(lambda x, y: x + y, arr) == sum:
                    res.append(arr.copy())
                arr.pop()
                return
            findPath(root.left, arr + [root.val])
            findPath(root.right, arr + [root.val])

        res = []
        findPath(root, [])
        return res


if __name__ == '__main__':
    arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    sum = 22
    root = Mock().arrToTreeNode(arr)
    print(Solution().pathSum(root, sum))
    print(Solution().pathSum2(root, sum))
