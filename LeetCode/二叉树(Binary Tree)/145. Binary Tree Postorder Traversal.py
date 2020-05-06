'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了37.00%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了7.41%的用户
        思路：先遍历root树，再右子树，最后左子树，即中右左，然后逆序，则变成左右中
             1
            / \
           2   3
        后序遍历：231
        先遍历根节点，再遍历右节点，再遍历左节点
        遇到这种二叉树的时候，可以就只画出3个节点，对照遍历即可。
        :param root:
        :return:
        '''
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
