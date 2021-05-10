"""
366. 寻找二叉树的叶子节点
给你一棵二叉树，请按以下要求的顺序收集它的全部节点：

依次从左到右，每次收集并删除所有的叶子节点
重复如上过程直到整棵树为空
 

示例:

输入: [1,2,3,4,5]
 
          1
         / \
        2   3
       / \
      4   5

输出: [[4,5,3],[2],[1]]
 

解释:

1. 删除叶子节点 [4,5,3] ，得到如下树结构：

          1
         /
        2
 

2. 现在删去叶子节点 [2] ，得到如下树结构：

          1
 

3. 现在删去叶子节点 [1] ，得到空树：

          []

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-leaves-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """
        思路：
        1. 自底向上递归，记录节点到叶节点之间不同深度的节点所在集合
        2. 通过哈希表实现，key,value分别对应接节点到叶节点的深度和节点的值的集合
        @param root:
        @return:
        """

        def dfs(root):
            if not root: return 0
            l, r = dfs(root.left), dfs(root.right)
            depth = max(l, r) + 1
            res[depth].append(root.val)
            return depth

        res = collections.defaultdict(list)
        dfs(root)
        return [v for k, v in res.items()]
