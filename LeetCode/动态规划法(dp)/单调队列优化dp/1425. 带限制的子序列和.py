"""
1425. 带限制的子序列和
给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 nums[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。

数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。

 

示例 1：

输入：nums = [10,2,-10,5,20], k = 2
输出：37
解释：子序列为 [10, 2, 5, 20] 。
示例 2：

输入：nums = [-1,-2,-3], k = 1
输出：-1
解释：子序列必须是非空的，所以我们选择最大的数字。
示例 3：

输入：nums = [10,-2,-10,-5,20], k = 2
输出：23
解释：子序列为 [10, -2, -5, 20] 。
 

提示：

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/constrained-subsequence-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        思路：dp+单调队列
        1. 涉及到区间求最值，可以考虑到单调队列
        @param nums:
        @param k:
        @return:
        """
        n = len(nums)
        queue = collections.deque()
        dp = [float('-inf')] * n
        for i, num in enumerate(nums):
            while queue and queue[0] + k < i:
                queue.popleft()
            if queue:
                dp[i] = max(0, dp[queue[0]]) + num
            else:
                dp[i] = num
            while queue and dp[i] > dp[queue[-1]]:
                queue.pop()
            queue.append(i)
        return max(dp)


if __name__ == '__main__':
    nums = [10, 2, -10, 5, 20]
    k = 2
    print(Solution().constrainedSubsetSum(nums, k))
