'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
通过次数26,604提交次数41,423

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了80.96%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了14.29%的用户
        :param root:
        :return:
        '''
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = [root.val]

        while queue:
            stack = []
            while queue:
                node = queue.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            if stack:
                queue = collections.deque(stack)
                res.append(stack[-1].val)
            else:
                break

        return res

    def rightSideView(self, root):
        if not root:
            return []
        level = [root]
        result = []
        while level:
            next_level = []
            result.append(level[-1].val)
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return result
