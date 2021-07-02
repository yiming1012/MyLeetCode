"""
面试题 04.09. 二叉搜索树序列
从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。给定一个由不同节点组成的二叉搜索树，输出所有可能生成此树的数组。

 

示例：
给定如下二叉树

        2
       / \
      1   3
返回：

[
   [2,1,3],
   [2,3,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bst-sequences-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root: return [[]]
        # 每次获取同一层可以遍历的节点

        def dfs(root, q, arr):
            if not root: return
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            if not q:
                res.append(arr.copy())
                return
            for i, node in enumerate(q):
                new = q[:i] + q[i + 1:]
                dfs(node, new, arr + [node.val])

        res = []
        dfs(root, [], [root.val])
        return res
