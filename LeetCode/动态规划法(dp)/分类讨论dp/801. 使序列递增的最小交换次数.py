"""
801. 使序列递增的最小交换次数
我们有两个长度相等且不为空的整型数组 A 和 B 。

我们可以交换 A[i] 和 B[i] 的元素。注意这两个元素在各自的序列中应该处于相同的位置。

在交换过一些元素之后，数组 A 和 B 都应该是严格递增的（数组严格递增的条件仅为A[0] < A[1] < A[2] < ... < A[A.length - 1]）。

给定数组 A 和 B ，请返回使得两个数组均保持严格递增状态的最小交换次数。假设给定的输入总是有效的。

示例:
输入: A = [1,3,5,4], B = [1,2,3,7]
输出: 1
解释:
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。
注意:

A, B 两个数组的长度总是相等的，且长度的范围为 [1, 1000]。
A[i], B[i] 均为 [0, 2000]区间内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        """
        思路：动态规划法
        1. 类似股票
        @param nums1:
        @param nums2:
        @return:
        """
        n = len(nums1)
        dp = [[float('inf')] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1, n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                # 1 3 5
                # 1 2 4
                if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1])
                    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + 1
                # 1 5 6
                # 1 2 4
                else:
                    dp[i][0] = dp[i - 1][0]
                    dp[i][1] = dp[i - 1][1] + 1

            # 1 2 5
            # 1 4 3
            else:
                dp[i][0] = dp[i - 1][1]
                dp[i][1] = dp[i - 1][0] + 1
        return min(dp[-1])

if __name__ == '__main__':
    A = [1, 3, 5, 4]
    B = [1, 2, 3, 7]