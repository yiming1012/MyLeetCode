"""
314. 二叉树的垂直遍历
给你一个二叉树的根结点，返回其结点按 垂直方向（从上到下，逐列）遍历的结果。

如果两个结点在同一行和列，那么顺序则为 从左到右。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[9],[3,15],[20],[7]]
示例 2：


输入：root = [3,9,8,4,0,1,7]
输出：[[4],[9],[3,0,1],[8],[7]]
示例 3：


输入：root = [3,9,8,4,0,1,7,null,null,null,2,5]
输出：[[4],[9,5],[3,0,1],[8,2],[7]]
示例 4：

输入：root = []
输出：[]
 

提示：

树中结点的数目在范围 [0, 100] 内
-100 <= Node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder1(self, root: TreeNode) -> List[List[int]]:
        """
        思路：BFS
        @param root:
        @return:
        """
        if not root: return []
        dic = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            root, index = queue.popleft()
            dic[index].append(root.val)
            if root.left:
                queue.append((root.left, index - 1))

            if root.right:
                queue.append((root.right, index + 1))
        res = []
        for k, v in sorted(dic.items(), key=lambda x: x[0]):
            res.append(v)
        return res

    def verticalOrder1(self, root: TreeNode) -> List[List[int]]:
        """
        思路：DFS
        @param root:
        @return:
        """
        if not root: return []
        dic = collections.defaultdict(list)

        def dfs(root, index, depth):
            if not root: return
            dic[index].append((depth, root.val))

            if root.left:
                dfs(root.left, index - 1, depth + 1)
            if root.right:
                dfs(root.right, index + 1, depth + 1)

        dfs(root, 0, 0)
        print(dic)
        res = []
        for k, v in sorted(dic.items(), key=lambda x: x[0]):
            print(v)
            res.append([b for a, b in sorted(v, key=lambda x: x[0])])
        return res
