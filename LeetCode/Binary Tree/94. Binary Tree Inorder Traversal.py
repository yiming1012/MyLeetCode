'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        执行用时 :32 ms, 在所有 Python3 提交中击败了88.76%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了7.84%的用户
        :param root:
        :return:
        '''
        if not root:
            return []
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res


if __name__ == '__main__':
    arr = [1, 2, 3]
    root = TreeNode(2)
    root.left = TreeNode(3)
    while root:
        print(root.val)
        root = root.left
    print(root)
    s = Solution()
    print(s.inorderTraversal(root))
