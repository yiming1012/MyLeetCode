'''
这个类的作用是将输入的数组构造成一棵树，并返回根节点，以供每次程序调用
'''

# Definition for a binary tree node.
from cmath import inf


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Mock:
    def arrToTreeNode(self, inputValues):
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
    root = Mock().arrToTreeNode(arr)
    print(root.val)
