'''
这个类的作用是将输入的数组构造成一棵树，并返回根节点，以供每次程序调用
'''

# Definition for a binary tree node.
from cmath import inf

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Mock:
    def arrToTreeNode(self, inputValues):
        root = TreeNode(int(inputValues[0]))
        queue = collections.deque([root])
        index = 1
        while index < len(inputValues):
            node = queue.popleft()
            item = inputValues[index]
            if item:
                node.left = TreeNode(item)
                queue.append(node.left)

            index = index + 1
            if index >= len(inputValues):
                break

            item = inputValues[index]
            if item:
                node.right = TreeNode(item)
                queue.append(node.right)
            index = index + 1
        return root


if __name__ == '__main__':
    arr = [5, 1, 4, None, None, 3, 6]
    root = Mock().arrToTreeNode(arr)


    def dfs(root):
        if not root:
            return
        print(root.val)
        dfs(root.left)
        dfs(root.right)


    dfs(root)
