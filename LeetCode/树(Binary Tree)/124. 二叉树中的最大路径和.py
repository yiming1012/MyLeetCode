"""
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        """
        题目明确说明了可能会有最大和路径不经过根节点的情况，这种时候的处理方式为：
        设立一个全局变量，在每次递归的时候讲经过根节点路径的最大值、不经过根节点的路径的最大值以及现存的全局最大值进行比较。
        最后在主函数中返回该值。
        时间复杂度：O(N)O(N)，其中 N 为树的节点个数。
        空间复杂度：O(h)O(h)，其中 h 为树的高度， 最坏的情况下树退化到链表，这个时候高度为 N，其中 N 为树的节点个数。
        """
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            #当前子树的maxSum挑战最大值
            self.res = max(self.res, max(l, 0) + max(r, 0) + node.val)
            # 向父节点提供的最大和，要包括自己
            return max(l, r, 0) + node.val

        dfs(root)
        return self.res
