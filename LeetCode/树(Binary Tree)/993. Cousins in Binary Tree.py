"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cousins-in-binary-tree
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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        思路：广度优先搜索（队列）
        1. 定义为堂兄弟，如果给定的两个数正好是左右节点，返回FALSE
        2. 如果某一层出现了一个，返回FALSE
        3. 如果某一层出现了两个，返回TRUE
        """
        if not root:
            return False
        queue = collections.deque()
        queue.append(root)
        while queue:
            count = 0
            for i in range(len(queue)):
                root = queue.popleft()
                if root.left and root.right:
                    if x in [root.left.val, root.right.val] and y in [root.left.val, root.right.val]:
                        return False
                if root.left:
                    queue.append(root.left)
                    if x == root.left.val or y == root.left.val:
                        count += 1
                if root.right:
                    queue.append(root.right)
                    if x == root.right.val or y == root.right.val:
                        count += 1
                if count == 2:
                    return True
                if count == 1:
                    return False
        return False

    def isCousins2(self, root: TreeNode, x: int, y: int) -> bool:
        """
        仿造官方题解
        1、
        """
        depth = {}
        father = {}

        def dfs(root, layer, pre):
            if not root:
                return
            depth[root.val] = layer
            father[root.val] = pre.val if pre else 0

            if root.left:
                dfs(root.left, layer + 1, root)

            if root.right:
                dfs(root.right, layer + 1, root)

        dfs(root, 0, None)
        return depth[x] == depth[y] and father[x] != father[y]

    def isCousins3(self, root, x, y):
        """
        官方题解思路：dfs+记忆化
        1. 利用两个dict记录每个节点的父节点和所在的层次
        2. 比较x,y所在层次以及父节点是否相同
        """
        parent = {}
        depth = {}

        def dfs(node, par=None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]
