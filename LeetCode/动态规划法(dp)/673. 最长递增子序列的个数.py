"""
673. 最长递增子序列的个数
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    tmp = dp[j] + 1
                    if tmp > dp[i]:
                        dp[i] = tmp
                        count[i] = count[j]
                    # 这个条件满足时，说明前面肯定出现过tmp
                    elif tmp == dp[i]:
                        count[i] += count[j]
        max_ = max(dp)
        res = 0
        for i in range(n):
            if dp[i] == max_:
                res += count[i]
        return res


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    print(Solution().findNumberOfLIS(nums))
