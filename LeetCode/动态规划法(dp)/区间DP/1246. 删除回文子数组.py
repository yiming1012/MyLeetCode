"""
1246. 删除回文子数组
给你一个整数数组 arr，每一次操作你都可以选择并删除它的一个 回文 子数组 arr[i], arr[i+1], ..., arr[j]（ i <= j）。

注意，每当你删除掉一个子数组，右侧元素都会自行向前移动填补空位。

请你计算并返回从数组中删除所有数字所需的最少操作次数。



示例 1：

输入：arr = [1,2]
输出：2
示例 2：

输入：arr = [1,3,4,1,5]
输出：3
解释：先删除 [4]，然后删除 [1,3,1]，最后再删除 [5]。


提示：

1 <= arr.length <= 100
1 <= arr[i] <= 20
"""
from typing import List


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for span in range(2, n + 1):
            for left in range(n - span + 1):
                right = left + span - 1
                if span == 2:
                    dp[left][right] = 1 if arr[left] == arr[right] else 2
                    continue
                # 判断两端是否相同
                if arr[left] == arr[right]:
                    dp[left][right] = dp[left + 1][right - 1]
                # 将数组分成两部分，计算两部分删除之和的最小值
                for k in range(left, right):
                    dp[left][right] = min(dp[left][right], dp[left][k] + dp[k + 1][right])

        return dp[0][-1]


if __name__ == '__main__':
    arr = [1, 2]
    print(Solution().minimumMoves(arr))
