"""
给你一个整数数组 arr 和一个整数值 target 。

请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。

请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。

 

示例 1：

输入：arr = [3,2,2,4,3], target = 3
输出：2
解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
示例 2：

输入：arr = [7,3,4,7], target = 7
输出：2
解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
示例 3：

输入：arr = [4,3,2,6,2,3,4], target = 6
输出：-1
解释：我们只有一个和为 6 的子数组。
示例 4：

输入：arr = [5,5,4,4,5], target = 3
输出：-1
解释：我们无法找到和为 3 的子数组。
示例 5：

输入：arr = [3,1,1,1,5,1,2,1], target = 3
输出：3
解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。
 

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
        思路：动态规划法
        1. 记录当前位置最短的target
        2. 当前target的长度与其开始的前一个位置上最短的target长度之和
        """
        dp = [float('inf')] * (len(arr) + 1)
        res = float('inf')
        presum = 0
        dic = collections.defaultdict()
        dic[0] = -1
        for i, num in enumerate(arr):
            presum += num
            dp[i + 1] = dp[i]
            if presum - target in dic:
                j = dic[presum - target]
                if dp[j + 1] != float('inf'):
                    res = min(res, dp[j + 1] + i - j)
                dp[i + 1] = min(i - j, dp[i])
            dic[presum] = i
        # print(dp)
        return res if res != float('inf') else -1


if __name__ == '__main__':
    arr = [3, 2, 2, 4, 3]
    target = 3
    print(Solution().minSumOfLengths(arr, target))
