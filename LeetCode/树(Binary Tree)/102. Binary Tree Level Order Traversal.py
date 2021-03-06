"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""

# Definition for a binary tree node.
import collections
from typing import List
from MockTreeNode import Mock


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        执行用时 :40 ms, 在所有 Python3 提交中击败了75.06%的用户
        内存消耗 :14 MB, 在所有 Python3 提交中击败了7.14%的用户
        思路：队列
        1、如果根节点为空，返回空列表
        2、从根节点开始，加入到队列，记录队列的大小n，即为这一层节点的个数。
        3、for循环遍历队列中前n个，并将每个节点的左右节点加入到队列
        4、在for循环中将每个节点加入到arr中，此轮for循环结束后将arr加入到res中

        """
        res = []
        if not root:
            return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            arr = []
            for i in range(size):
                root = queue.popleft()
                arr.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(arr)
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """
        执行用时 :44 ms, 在所有 Python3 提交中击败了55.95%的用户
        内存消耗 :14.5 MB, 在所有 Python3 提交中击败了7.14%的用户
        思路：dfs
        """

        def dfs(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)

        res = []
        print(res)
        dfs(root, 0)
        return res

    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        """
        优秀代码
        """
        if root is None:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)
        step = -1
        while queue:
            step += 1
            result.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                result[step].append(node.val)
                for neighbor in (node.left, node.right):
                    if neighbor is not None:
                        queue.append(neighbor)

        return result


if __name__ == '__main__':
    arr = [5, 1, 4, None, None, 3, 6]
    root = Mock().arrToTreeNode(arr)
    print(Solution().levelOrder3(root))
    print(root.val)
