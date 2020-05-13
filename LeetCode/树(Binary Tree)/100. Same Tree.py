'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from MockTreeNode import Mock


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        执行用时 :44 ms, 在所有 Python3 提交中击败了41.40%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了7.14%的用户
        思路：递归
        1. 两棵树相同的充要条件是：根节点和左右子树都相等
        2. 递归条件：p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        3. 退出条件：两个节点是否相等，或一个为空，另一个不为空
        """

        # 两个都为空，相同
        if not p and not q:
            return True
        # 有一个为空，不同
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        """
        思路：
        1. 利用树的遍历将树的每一个节点加入到数组中
        2. 由于树的形状不一样可能遍历结果会相同。如[1,2]和[1,None,2]的先序遍历都是1->2,这里需要将将整棵树想象成一棵完全二叉树
        3. 将为空的子树用特殊符号填充，如'#'。然后比较两个数组是否相同
        """
        if not p and not q:
            return True

        def dfs(node, arr):
            if not node:
                arr.append('#')
                return
            arr.append(str(node.val))
            dfs(node.left, arr)
            dfs(node.right, arr)

        arr1 = []
        arr2 = []
        dfs(p, arr1)
        dfs(q, arr2)
        print(arr1)
        print(arr2)
        # is比较的是id
        # == 比较的是值
        return arr1 == arr2


if __name__ == '__main__':
    arr1 = [1, 2, 3]
    arr2 = [1, None, 2]
    # 将数组转换为树形结构
    a = Mock().arrToTreeNode(arr1)
    b = Mock().arrToTreeNode(arr2)
    print(Solution().isSameTree2(a, b))
