"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subtree-of-another-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        这种利用遍历，形成字符串的方法是错误的
        因为：'1' in '12',但很明显这不是一样的
        """
        # 如果都为空，满足条件
        if not s and not t:
            return True

        def dfs(node, arr):
            if not node:
                arr.append('#')
                return
            arr.append(str(node.val))
            dfs(node.left, arr)
            dfs(node.right, arr)

        arr1 = ['#']
        arr2 = ['#']
        dfs(s, arr1)
        dfs(t, arr2)
        print(arr1)
        print(arr2)

        # is比较的是id
        # == 比较的是值
        # 不能用这种方式，因为'2' in '12'
        return ",".join(arr2) in ",".join(arr1)

    def isSubtree2(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



