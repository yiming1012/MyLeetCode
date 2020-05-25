"""
给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。

 

示例 1：



输入：root = [2,3,1,3,1,null,1]
输出：2
解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
     在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。
示例 2：



输入：root = [2,1,1,1,3,null,null,null,null,null,1]
输出：1
解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
     这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。
示例 3：

输入：root = [9]
输出：1
 

提示：

给定二叉树的节点数目在 1 到 10^5 之间。
节点值在 1 到 9 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if not root:
            return 1
        res = []

        def search(root, arr):
            if not root.left and not root.right:
                res.append(arr.copy())
                return
            if root.left:
                search(root.left, arr + [root.left.val])
            if root.right:
                search(root.right, arr + [root.right.val])

        search(root, [root.val])
        ans = 0
        for l in res:
            dic = collections.Counter(l)
            count = 0
            for k, v in dic.items():
                if v & 1:
                    count += 1
            if count <= 1:
                ans += 1

        return ans

    def pseudoPalindromicPaths2(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return 0

        def get1bit(n):
            # 计算一个数字1的位数
            res = 0
            while n:
                n &= n - 1
                res += 1
            return res

        def dfs(node, mask):
            if not node.left and not node.right:
                # 叶子节点, 且奇数个数的元素数目不大于1就是满足条件的路径
                if get1bit(mask) <= 1:
                    self.res += 1
                return
            if node.left:
                dfs(node.left, mask ^ (1 << node.left.val))
            if node.right:
                dfs(node.right, mask ^ (1 << node.right.val))

        dfs(root, 1 << root.val)
        return self.res
