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
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
        1.本题采用动态规划比较好理解, 用dp[i]记录从第i个元素(包含第i个)往前找到的和为target最短子数组长度,
        2.同时用一个字典sum_record记录从头到尾遍历时候遇到的总和及其相应位置。
        3.每到一个位置i上的数, 先把dp[i]设置为dp[i-1], 然后之前当前的总和减去之前的子数组的总和为target是否存在,
        4.为了减少判断, 我们先把0: -1放到字典中, 如果存在, 则找到该区间起点, 起点为sum_record[sums-target],
        此时可以得到当前和为target的子数组的长度cur_len, 然后去dp数组里获取i-cur_len之前保存的另一部分和为target的最短子数组长度,
        进行结果的更新, 并更新dp[i];
        """
        n = len(arr)
        # dp[i]记录从第i个元素(包含第i个)往前找到的和为target最短子数组长度
        dp = [float("inf")] * n
        sums, ans = 0, float("inf")
        # sum_record记录和为target的子数组位置
        sum_record = {0: -1}
        for i, num in enumerate(arr):
            sums += num
            dp[i] = dp[i-1]
            if sums - target in sum_record:
                cur_len = i - sum_record[sums-target]
                if i - cur_len >= 0:
                    ans = min(ans, cur_len + dp[i-cur_len])
                dp[i] = min(dp[i-1], cur_len)
            sum_record[sums] = i
        return ans if ans != float("inf") else -1

