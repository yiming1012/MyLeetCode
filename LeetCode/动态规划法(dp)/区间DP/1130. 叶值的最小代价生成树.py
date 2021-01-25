"""
1130. 叶值的最小代价生成树
给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：

每个节点都有 0 个或是 2 个子节点。
数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。（知识回顾：如果一个节点有 0 个子节点，那么该节点为叶节点。）
每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。

 

示例：

输入：arr = [6,2,4]
输出：32
解释：
有两种可能的树，第一种的非叶节点的总和为 36，第二种非叶节点的总和为 32。

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
 

提示：

2 <= arr.length <= 40
1 <= arr[i] <= 15
答案保证是一个 32 位带符号整数，即小于 2^31。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def mctFromLeafValues1(self, arr: List[int]) -> int:
        n = len(arr)
        max_ = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                max_[i][j] = max(arr[i:j + 1])

        dp = [[float('inf')] * n for _ in range(n)]
        dp[0][0] = 0
        for i in range(1, n):
            dp[i][i] = 0
            dp[i - 1][i] = arr[i] * arr[i - 1]
        for span in range(3, n + 1):
            for i in range(n - span + 1):
                j = i + span - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max_[i][k] * max_[k + 1][j])
        return dp[0][-1]

    def mctFromLeafValues2(self, A: List[int]) -> int:
        # 从中间找两边较小值，用单调栈
        res, n = 0, len(A)
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res


if __name__ == '__main__':
    arr = [6, 2, 4]
    print(Solution().mctFromLeafValues1(arr))
    print(Solution().mctFromLeafValues2(arr))
