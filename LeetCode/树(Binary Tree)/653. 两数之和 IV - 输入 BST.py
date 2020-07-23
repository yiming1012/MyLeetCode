"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget1(self, root: TreeNode, k: int) -> bool:
        """
        思路：回溯+剪枝
        """
        def recur(root, k, hashset):
            if not root:
                return False
            target = k - root.val
            if target in hashset:
                return True
            else:
                hashset.add(root.val)
            return recur(root.left, k, hashset) or recur(root.right, k, hashset)

        hashset = set()
        return recur(root, k, hashset)

    def findTarget2(self, root: TreeNode, k: int) -> bool:
        """
        思路：通过flag来标记是否已找到
        """
        if not root:
            return []
        dic = set()
        flag = False

        def inorder(root):
            if root:
                inorder(root.left)
                if k - root.val in dic:
                    nonlocal flag
                    flag = True
                    return
                dic.add(root.val)
                inorder(root.right)

        inorder(root)
        return flag
