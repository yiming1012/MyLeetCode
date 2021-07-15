"""
889. 根据前序和后序遍历构造二叉树
返回与给定的前序和后序遍历匹配的任何二叉树。

 pre 和 post 遍历中的值是不同的正整数。

 

示例：

输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]
 

提示：

1 <= pre.length == post.length <= 30
pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def dfs(pre, post):
            if len(pre) == 1:
                return TreeNode(pre[0])
            root = TreeNode(pre[0])
            left = pre[1]
            right = post[-2]
            # 判断是否只剩一颗子树
            if left == right:
                # 只有一棵子树
                root.left = dfs(pre[1:], post[:-1])
            else:
                # 存在左右子树
                # 分别找到左右子树的根节点
                prel = pre.index(right)
                postl = post.index(left)
                root.left = dfs(pre[1:prel], post[:postl + 1])
                root.right = dfs(pre[prel:], post[postl + 1:-1])

            return root

        return dfs(pre, post)
