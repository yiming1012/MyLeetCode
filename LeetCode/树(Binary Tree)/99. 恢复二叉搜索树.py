"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
进阶:

使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree1(self, root: TreeNode) -> None:
        """
        思路：二叉搜索树中序遍历的结果应该是从小到大排好序的
        1. 中序遍历获取每个节点root
        2. 将节点的值排序
        3. 将节点的对象和值一一对应
        @param root:
        @return:
        """

        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root)
                inorder(root.right)

        res = []
        inorder(root)
        value = [node.val for node in res]
        value.sort()
        for i in range(len(res)):
            res[i].val = value[i]

    def recoverTree2(self, root: TreeNode) -> None:
        """
        关键点：两个交换的元素会构成两个（或一个）逆序对
        @param root:
        @return:
        """

        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root)
                inorder(root.right)

        res = []
        inorder(root)

        first = None
        second = None
        for i in range(1, len(res)):
            if res[i].val < res[i - 1].val:
                if first is None:
                    first = res[i - 1]
                    second = res[i]
                else:
                    second = res[i]
                    break
        first.val, second.val = second.val, first.val

    def recoverTree3(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        pre = None
        first, second = None, None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre is not None and pre.val > root.val:
                if first is None:
                    first = pre
                    second = root
                else:
                    second = root
                    break
            pre = root
            root = root.right
        first.val, second.val = second.val, first.val

    def recoverTree4(self, root: TreeNode) -> None:
        """
        思路：Morris遍历，让空间复杂度为O(1)
        """
        if not root: return
        p = root
        prenode = None
        pre = None
        first, second = None, None
        while p:
            if p.left:
                prenode = p.left
                while prenode.right and prenode.right != p:
                    prenode = prenode.right
                if not prenode.right:  # 建立链接方便回溯
                    prenode.right = p
                    p = p.left
                    continue
                if prenode.right == p:
                    prenode.right = None  # 回溯完成删除多余链接

            if pre and pre.val > p.val:
                if not first:
                    first = pre
                    second = p
                else:
                    second = p

            pre = p
            p = p.right
        first.val, second.val = second.val, first.val