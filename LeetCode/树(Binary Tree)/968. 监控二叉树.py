"""
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。

 

示例 1：



输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。
示例 2：



输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

提示：

给定树的节点数的范围是 [1, 1000]。
每个节点的值都是 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-cameras
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0

        # 1.该节点安装摄像头 2.没安装，但被监控 3.该节点没有被监控，所以父节点必须安装
        def dfs(node: TreeNode):
            if not node:
                return 2
            left, right = dfs(node.left), dfs(node.right)
            if left == 3 or right == 3:
                nonlocal ans
                ans += 1
                return 1
            elif left == 1 or right == 1:
                return 2
            else:
                # 条件等同于左右都是2状态
                return 3

        # 再往上没有了，所以必须把root节点安装上摄像头
        if dfs(root) == 3:
            ans += 1
        return ans
