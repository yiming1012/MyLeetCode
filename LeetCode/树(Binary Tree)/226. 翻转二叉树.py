"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from MockTreeNode import Mock
from TreeNodeToArr import TreeNodeToArr


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        思路：先序遍历
        关键：将每个点的左右子节点交换
        """
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        思路：中序遍历
        关键：将每个点的左右子节点交换
        """
        if not root:
            return root
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        return root


if __name__ == '__main__':
    arr = [4, 2, 7, 1, 3, 6, 9]
    arr = [1, 2, 3, None, 4]
    root = Mock().arrToTreeNode(arr)
    pre = Solution().invertTree(root)
    print(TreeNodeToArr().treeNodeToString(pre))
