'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
from typing import List
from MockTreeNode import Mock
'''
pycharm消除.py文件中import自己包出现红色波浪线（执行正常）
解决方法：file——setting——project：xxx——project structure——选中.py模块所在路径点击“source”——ok
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = 0
    count = 0
    last = None
    # 输出结果的数组不算额外空间
    ans = []

    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return
        self.findMode(root.left)
        if root.val == self.last:
            self.count += 1
        else:
            self.last = root.val
            self.count = 1

        if self.res == self.count:
            self.ans.append(self.last)
        elif self.res < self.count:
            self.ans.clear()
            self.ans.append(self.last)
            self.res = self.count

        self.findMode(root.right)
        return self.ans


if __name__ == '__main__':
    arr = [1, None, 2, 2]
    root = Mock().arrToTreeNode(arr)
    print("root: ", root.val)
    print(Solution().findMode(root))
