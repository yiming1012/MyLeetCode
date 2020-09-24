"""
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
 

注意: 您可以假设树（即给定的根节点）不为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-bottom-left-tree-value
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue1(self, root: TreeNode) -> int:
        """
        思路：层次遍历
        1. 求最后一层最左边的点，可以通过层次遍历
        @param root:
        @return:
        """
        res = None
        queue = collections.deque()
        queue.append(root)
        while queue:
            root = queue.popleft()
            res = root.val
            if root.right:
                queue.append(root.right)
            if root.left:
                queue.append(root.left)
        return res

    def findBottomLeftValue2(self, root: TreeNode) -> int:
        """
        思路：DFS
        1. 每次进到下一层的肯定是最左边的点，如果是同一层的就不会比较，比最大层还深，就重新记录
        @param root:
        @return:
        """

        res = None
        maxDepth = -1

        def dfs(root, i):
            if not root:
                return
            nonlocal maxDepth, res
            if i > maxDepth:
                res = root.val
                maxDepth = i
            dfs(root.left, i + 1)
            dfs(root.right, i + 1)

        dfs(root, 0)
        return res
