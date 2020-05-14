"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a Node.
import collections
from typing import List
from MockTreeNode import Mock


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        思路：
        1. 将所有元素通过队列存储
        2. 每次记录下层的个数进行遍历
        """
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            arr = []
            for _ in range(len(queue)):
                root = queue.popleft()
                arr.append(root.val)
                if root.children:
                    queue.extend(root.children)
            res.append(arr)
        return res

    def levelOrder2(self, root: 'Node') -> List[List[int]]:
        """
        优秀答案
        思路：
        1. 每个节点有多个孩子，即root.children为一个列表
        2. 每一层通过extend将子孩子列表的元素添加到下一层的列表中
        3. 本层节点和下层节点分别用两个列表存储
        """
        if not root:
            return []

        output = []
        stack = [root]

        while stack:
            temp = []
            output.append([])
            for i in stack:
                temp.extend(i.children)
                output[-1].append(i.val)
            stack = temp
        return output
