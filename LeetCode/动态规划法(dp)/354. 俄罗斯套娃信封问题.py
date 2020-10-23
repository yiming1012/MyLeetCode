"""
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/russian-doll-envelopes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from bisect import bisect_left

class Solution:
    def maxEnvelopes1(self, envelopes: List[List[int]]) -> int:
        """
        思路：动态规划法+最长上升子序列
        @param envelopes:
        @return:
        """
        if not envelopes:
            return 0
        envelopes.sort()
        n = len(envelopes)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            a, b = envelopes[i]
            for j in range(i):
                c, d = envelopes[j]
                if a > c and b > d:
                    dp[i] = max(dp[i], dp[j] + 1)

            res = max(res, dp[i])
        return res


    def maxEnvelopes2(self, arr: List[List[int]]) -> int:
        # sort increasing in first dimension and decreasing on second
        arr.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
        return lis([i[1] for i in arr])


if __name__ == '__main__':
    envelopes = [[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]
    print(Solution().maxEnvelopes1(envelopes))
    print(Solution().maxEnvelopes2(envelopes))
