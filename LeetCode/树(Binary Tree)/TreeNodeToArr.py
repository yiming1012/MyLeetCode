# Definition for a binary tree node.
import collections
from typing import List
from MockTreeNode import Mock


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeNodeToArr:
    def treeNodeToString(self, root):
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            node = queue.popleft()
            if not node:
                res.append(None)
                continue

            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        while res and res[-1] is None:
            res.pop()

        return res


if __name__ == '__main__':
    arr = [1, 2, 3, None, None, 4, 5]
    pre = Mock().arrToTreeNode(arr)
    print(TreeNodeToArr().treeNodeToString(pre))
