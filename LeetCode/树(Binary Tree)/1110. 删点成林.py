"""
1110. 删点成林
给出二叉树的根节点 root，树上每个节点都有一个不同的值。

如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

返回森林中的每棵树。你可以按任意顺序组织答案。

 

示例：



输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
输出：[[1,2,null,4],[6],[7]]
 

提示：

树中的节点数最大为 1000。
每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
to_delete.length <= 1000
to_delete 包含一些从 1 到 1000、各不相同的值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-nodes-and-return-forest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        dic = set(to_delete)
        res = []
        if not root: return res
        if root.val not in dic:
            res.append(root)

        def dfs(root):
            if not root: return
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if not root or root.val in dic:
                if root.left: res.append(root.left)
                if root.right: res.append(root.right)
                return None
            return root

        dfs(root)
        return res
