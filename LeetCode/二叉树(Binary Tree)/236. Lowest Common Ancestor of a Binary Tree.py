"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

解题思路：
祖先的定义： 若节点 pp 在节点 rootroot 的左（右）子树中，或 p = rootp=root ，则称 rootroot 是 pp 的祖先。
最近公共祖先的定义： 设节点 rootroot 为节点 p, qp,q 的某公共祖先，若其左子节点 root.leftroot.left 和右子节点 root.rightroot.right 都不是 p,qp,q 的公共祖先，则称 rootroot 是 “最近的公共祖先” 。

根据以上定义，若 rootroot 是 p, qp,q 的 最近公共祖先 ，则只可能为以下情况之一：

pp 和 qq 在 rootroot 的子树中，且分列 rootroot 的 异侧（即分别在左、右子树中）；
p = rootp=root ，且 qq 在 rootroot 的左或右子树中；
q = rootq=root ，且 pp 在 rootroot 的左或右子树中；


考虑通过递归对二叉树进行后序遍历，当遇到节点 pp 或 qq 时返回。从底至顶回溯，当节点 p, qp,q 在节点 rootroot 的异侧时，节点 rootroot 即为最近公共祖先，则向上返回 rootroot 。

递归解析：
终止条件：
当越过叶节点，则直接返回 nullnull ；
当 rootroot 等于 p, qp,q ，则直接返回 rootroot ；
递推工作：
开启递归左子节点，返回值记为 leftleft ；
开启递归右子节点，返回值记为 rightright ；
返回值： 根据 leftleft 和 rightright ，可展开为四种情况；
当 leftleft 和 rightright 同时为空 ：说明 rootroot 的左 / 右子树中都不包含 p,qp,q ，返回 nullnull ；
当 leftleft 和 rightright 同时不为空 ：说明 p, qp,q 分列在 rootroot 的 异侧 （分别在 左 / 右子树），因此 rootroot 为最近公共祖先，返回 rootroot ；
当 leftleft 为空 ，rightright 不为空 ：p,qp,q 都不在 rootroot 的左子树中，直接返回 rightright 。具体可分为两种情况：
p,qp,q 其中一个在 rootroot 的 右子树 中，此时 rightright 指向 pp（假设为 pp ）；
p,qp,q 两节点都在 rootroot 的 右子树 中，此时的 rightright 指向 最近公共祖先节点 ；
当 leftleft 不为空 ， rightright 为空 ：与情况 3. 同理；
观察发现， 情况 1. 可合并至 3. 和 4. 内，详见文章末尾代码。


1 / 18

复杂度分析：
时间复杂度 O(N)O(N) ： 其中 NN 为二叉树节点数；最差情况下，需要递归遍历树的所有节点。
空间复杂度 O(N)O(N) ： 最差情况下，递归深度达到 NN ，系统使用 O(N)O(N) 大小的额外空间。
代码：
pythonjava
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
情况 1. , 2. , 3. , 4. 的展开写法如下。

pythonjava
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return # 1.
        if not left: return right # 3.
        if not right: return left # 4.
        return root # 2. if left and right:


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
此题有两种解法
1. 递归
2. 存储父节点
"""


class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        思路：存储父节点
        """
        dic = {root: None}

        def dfs(node):
            if node:
                if node.left:
                    dic[node.left] = node
                if node.right:
                    dic[node.right] = node
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        l1, l2 = p, q
        while l1 != l2:
            l1 = dic.get(l1, q)
            l2 = dic.get(l2, p)
        return l1

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        思路：递归
        """
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
