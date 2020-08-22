"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        思路：自底向上递归
        1. 当某个节点不平衡时，返回-1，很巧妙
        2. 每个节点的高度等于左右子树高度+1
        @param root:
        @return:
        """
        if not root:
            return True

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1 or abs(right - left) > 1:
                return -1
            return max(left, right) + 1

        return dfs(root) >= 0


class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        思路：自顶向下的递归
        1. 对每一个节点进行判断是否达到平衡
        2. 对于每一个点在递归过程中会重复利用，复杂度较高
        时间复杂度：O(N*N)
        空间复杂度：O(N)
        @param root:
        @return:
        """
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def height(self, node):
        if not node:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        return max(left, right) + 1
