"""
5711. 有界数组中指定下标处的最大值
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

nums.length == n
nums[i] 是 正整数 ，其中 0 <= i < n
abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
nums 中所有元素之和不超过 maxSum
nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。

注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。



示例 1：

输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
示例 2：

输入：n = 6, index = 1,  maxSum = 10
输出：3


提示：

1 <= n <= maxSum <= 109
0 <= index < n
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def check(x):

            left = min(x, index + 1)
            right = min(x, n - index)
            pre = (x + x - left + 1) * left // 2
            suf = (x + x - right + 1) * right // 2
            return pre + suf - x + (n - left - right + 1) <= maxSum

        l, r = 1, maxSum
        while l < r:
            mid = l + (r - l + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
