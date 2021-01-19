"""
1186. 删除一次得到子数组最大和
给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。

换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。

注意，删除一个元素后，子数组 不能为空。

请看示例：

示例 1：

输入：arr = [1,-2,0,3]
输出：4
解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。
示例 2：

输入：arr = [1,-2,-2,3]
输出：3
解释：我们直接选出 [3]，这就是最大和。
示例 3：

输入：arr = [-1,-1,-1,-1]
输出：-1
解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
     我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。


提示：

1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4
"""
from typing import List


class Solution:
    def maximumSum1(self, arr: List[int]) -> int:
        """
        思路：动态规划法
        dp[i][0]：不删除元素，以i结尾的最大值
        dp[i][1]：删除其中一个得到的最大值，有两种情况（1，删除i 2. 不删除i）
        @param arr:
        @return:
        """
        n = len(arr)
        dp = [[float('-inf')] * 2 for _ in range(n + 1)]
        ans = float('-inf')
        for i in range(n):
            dp[i + 1][0] = max(dp[i][0] + arr[i], arr[i])
            dp[i + 1][1] = max(dp[i][1] + arr[i], dp[i][0])
            ans = max(ans, dp[i + 1][0], dp[i + 1][1])
        return ans

    def maximumSum2(self, arr: List[int]) -> int:
        n = len(arr)
        ans = float('-inf')
        a, b = float('-inf'), float('-inf')
        for i in range(n):
            a, b = max(a + arr[i], arr[i]), max(b + arr[i], a)
            ans = max(ans, a, b)
        return ans

    def maximumSum3(self, arr: List[int]) -> int:
        """
        思路：
        1. left[i]为从左到右以i结尾的子数组最大和
        2. right[i]为从右到左以i结尾的子数组最大和
        3. 最后的结果：
            1. 不删除：max(left)
            2. 删除：left[i - 1] + right[i + 1]的最大值
        @param arr:
        @return:
        """
        n = len(arr)
        left = [float('-inf')] * n
        right = [float('-inf')] * n
        left[0] = arr[0]
        right[-1] = arr[-1]
        for i in range(1, n):
            left[i] = max(left[i - 1] + arr[i], arr[i])
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1] + arr[i], arr[i])
        res = max(left)
        for i in range(1, n - 1):
            res = max(res, left[i - 1] + right[i + 1])
        return res


if __name__ == '__main__':
    arr = [1, -2, 0, 3]
    print(Solution().maximumSum1(arr))
    print(Solution().maximumSum2(arr))
