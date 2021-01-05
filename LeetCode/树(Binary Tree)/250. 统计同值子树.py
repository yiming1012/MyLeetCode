"""
250. 统计同值子树
给定一个二叉树，统计该二叉树数值相同的子树个数。

同值子树是指该子树的所有节点都拥有相同的数值。

示例：

输入: root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-univalue-subtrees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            if not root: return None
            left = dfs(root.left)
            right = dfs(root.right)
            if (not left and not right) or (left and right and left == right == root.val) or (
                    not left and right == root.val) or (not right and left == root.val):
                nonlocal res
                res += 1
                return root.val
            else:
                return float('inf')

        dfs(root)
        return res


