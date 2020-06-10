'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
from typing import List
from MockTreeNode import Mock


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    res=[]
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了16.32%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了7.14%的用户
        思路：先序遍历，先遍历根节点-左子树-右子树
        入栈顺序：根节点弹出-右子树入栈-左子树入栈
        :param root:
        :return:
        '''
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res