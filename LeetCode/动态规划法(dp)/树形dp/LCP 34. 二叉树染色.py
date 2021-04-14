"""
LCP 34. 二叉树染色
小扣有一个根结点为 root 的二叉树模型，初始所有结点均为白色，可以用蓝色染料给模型结点染色，模型的每个结点有一个 val 价值。小扣出于美观考虑，希望最后二叉树上每个蓝色相连部分的结点个数不能超过 k 个，求所有染成蓝色的结点价值总和最大是多少？

示例 1：

输入：root = [5,2,3,4], k = 2

输出：12

解释：结点 5、3、4 染成蓝色，获得最大的价值 5+3+4=12


示例 2：

输入：root = [4,1,3,9,null,null,2], k = 2

输出：16

解释：结点 4、3、9 染成蓝色，获得最大的价值 4+3+9=16


提示：

1 <= k <= 10
1 <= val <= 10000
1 <= 结点数量 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-ran-se-UGC
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:

        def dfs(root):
            dp = [0] * (k + 1)
            if not root: return dp
            L = dfs(root.left)
            R = dfs(root.right)
            # 不选
            dp[0] = max(L) + max(R)
            # 选
            for i in range(k):
                for j in range(k):
                    if i + j + 1 <= k:
                        dp[i + j + 1] = max(dp[i + j + 1], L[i] + R[j] + root.val)
            return dp

        res = dfs(root)
        return max(res)
