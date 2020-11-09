"""
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

 

示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
 

提示：

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ones-and-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        """
        思路：记忆化递归
        @param strs:
        @param m:
        @param n:
        @return:
        """
        length = len(strs)
        arr = [(word.count("1"), word.count("0")) for word in strs]
        memo = {}

        def dfs(one, zero, index):
            if index == length:
                return 0
            if (one, zero, index) in memo:
                return memo[(one, zero, index)]

            ans = 0
            cnt1, cnt0 = arr[index]
            # 选择
            if one + cnt1 <= n and zero + cnt0 <= m:
                ans = 1 + dfs(one + cnt1, zero + cnt0, index + 1)
            # 不选
            ans = max(ans, dfs(one, zero, index + 1))
            memo[(one, zero, index)] = ans
            return ans

        return dfs(0, 0, 0)

    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        """
        思路：动态规划法
        @param strs:
        @param m:
        @param n:
        @return:
        """
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for word in strs:
            one = word.count("1")
            zero = word.count("0")
            for i in range(n, one - 1, -1):
                for j in range(m, zero - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - one][j - zero] + 1)

        return dp[-1][-1]


if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(Solution().findMaxForm1(strs, m, n))
    print(Solution().findMaxForm2(strs, m, n))
