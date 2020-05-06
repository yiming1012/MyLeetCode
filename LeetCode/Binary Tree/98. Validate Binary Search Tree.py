'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
from cmath import inf


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = inf
        # left = -float('inf')
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= left:
                return False
            left = root.val
            root = root.right
        return True


class Solution2:
    last = float('inf')

    def isValidBST(self, root: TreeNode) -> bool:
        """
        思路: 中序遍历  因为二叉搜索树的中序遍历是升序或者降序排列
        """
        if root is None: return True

        if not self.isValidBST(root.left):
            return False
        if self.last and root.val <= self.last:
            return False
        self.last = root.val

        if not self.isValidBST(root.right):
            return False
        return True

    def arrToTreeNode(self,inputValues):
        root = TreeNode(int(inputValues[0]))
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1

            item = inputValues[index]
            index = index + 1
            if item:
                node.left = TreeNode(item)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if item:
                node.right = TreeNode(item)
                nodeQueue.append(node.right)
        return root


if __name__ == '__main__':
    arr = [5, 1, 4, None, None, 3, 6]
    root=Solution2().arrToTreeNode(arr)
    print(root.val)
    print(Solution2().isValidBST(root))

