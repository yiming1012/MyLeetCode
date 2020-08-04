"""
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    nex = None

    def flatten(self, root: TreeNode) -> None:
        """
        思路：
        1. 记录中间变量
        """
        if root:
            self.flatten(root.right)
            self.flatten(root.left)
            print(root.val)
            root.right = self.nex
            root.left = None
            self.nex = root

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        def dfs(root):
            if root:
                arr.append(root)
                dfs(root.left)
                dfs(root.right)

        arr = []
        dummy = root
        dfs(root)
        for i in range(len(arr) - 1):
            arr[i].left = None
            arr[i].right = arr[i + 1]
        return dummy

