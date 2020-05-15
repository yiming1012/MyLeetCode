"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        执行用时 :52 ms, 在所有 Python3 提交中击败了80.43%的用户
        内存消耗 :14.9 MB, 在所有 Python3 提交中击败了12.50%的用户
        思路：
        1、树的最小深度指的是，从根节点到叶子节点的高度
        2、叶子节点即左右子节点都为空
        3、层次遍历，遇到叶子节点则返回高度
        """
        if not root:
            return 0
        queue = collections.deque()
        queue.append(root)
        count = 1
        while queue:
            for _ in range(len(queue)):
                root = queue.popleft()
                if not root.left and not root.right:
                    return count
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            else:
                count += 1

    def minDepth2(self, root: TreeNode) -> int:
        """
        思路：递归
        1、如果节点空，返回深度为0
        2、如果左子树为空，则遍历右子树
        3、如果右子树为空，则遍历左子树
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1