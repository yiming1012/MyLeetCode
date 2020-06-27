"""
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

示例 1:

输入:
    2
   / \
  2   5
     / \
    5   7

输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。
示例 2:

输入:
    2
   / \
  2   2

输出: -1
说明: 最小的值是 2, 但是不存在第二小的值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree
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
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        first = root.val
        second = float('inf')
        queue = collections.deque()
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.val > first:
                    second = min(second, node.val)
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)

        return -1 if second == float('inf') else second

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        return self.helper(root, root.val)

    def helper(self, root, value):
        if not root:
            return -1
        if root.val > value:
            return root.val
        l = self.helper(root.left, value)
        r = self.helper(root.right, value)
        if l == -1:
            return r
        if r == -1:
            return l
        return min(r, l)
