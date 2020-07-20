"""
解题思路
一、采用DFS深度优先遍历算法
用三个下边分别标识s1, s2, s3，然后进行匹配，直到匹配成功。代码清晰易读，注释详细。

二、DP动态规划法
假设dp[i][j]表示s1前i个字符和s2前j个字符，能否和s3的前(i+j)个字符匹配
则转移方程为：dp[i][j]=(dp[i-1][j] and s1[i] == s3[i+1]) or (dp[i][j-1] and s2[j] == s3[i+j])
初始状态为：dp[0][0] = True

"""

# DFS缓存
from functools import lru_cache


class Solution:
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        # 边界情况
        if len(s1) + len(s2) != len(s3):
            return False

        # 因为有重复计算，需要增加缓存
        @lru_cache()
        def dfs(i, j, k):
            # 递归结束条件
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if i > len(s1) or j > len(s2) or k > len(s3):
                return False

            # s1 和 s3 的字符相匹配
            if i < len(s1) and k < len(s3) and s1[i] == s3[k] and dfs(i + 1, j, k + 1):
                return True

            # s2 和 s3 的字符相匹配
            if j < len(s2) and k < len(s3) and s2[j] == s3[k] and dfs(i, j + 1, k + 1):
                return True

            return False

        return dfs(0, 0, 0)

    # DP动态规划
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        rows, cols = len(s1) + 1, len(s2) + 1
        dp = [[False] * cols for _ in range(rows)]
        dp[0][0] = True
        for i in range(rows):
            for j in range(cols):
                k = i + j - 1
                if i > 0:
                    dp[i][j] |= (dp[i - 1][j] and s1[i - 1] == s3[k])
                if j > 0:
                    dp[i][j] |= (dp[i][j - 1] and s2[j - 1] == s3[k])
        return dp[-1][-1]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(Solution().isInterleave1(s1, s2, s3))
    print(Solution().isInterleave2(s1, s2, s3))