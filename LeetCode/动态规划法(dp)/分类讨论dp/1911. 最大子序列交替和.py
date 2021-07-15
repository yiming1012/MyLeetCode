"""
1911. 最大子序列交替和
一个下标从 0 开始的数组的 交替和 定义为 偶数 下标处元素之 和 减去 奇数 下标处元素之 和 。

比方说，数组 [4,2,5,3] 的交替和为 (4 + 5) - (2 + 3) = 4 。
给你一个数组 nums ，请你返回 nums 中任意子序列的 最大交替和 （子序列的下标 重新 从 0 开始编号）。

一个数组的 子序列 是从原数组中删除一些元素后（也可能一个也不删除）剩余元素不改变顺序组成的数组。比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的一个子序列（加粗元素），但是 [2,4,2] 不是。

 

示例 1：

输入：nums = [4,2,5,3]
输出：7
解释：最优子序列为 [4,2,5] ，交替和为 (4 + 5) - 2 = 7 。
示例 2：

输入：nums = [5,6,7,8]
输出：8
解释：最优子序列为 [8] ，交替和为 8 。
示例 3：

输入：nums = [6,2,1,2,4,5]
输出：10
解释：最优子序列为 [6,1,5] ，交替和为 (6 + 5) - 1 = 10 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-alternating-subsequence-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # dp[i][0]:以i结尾的为偶数下标
        # dp[i][1]:以i结尾的为奇数下标
        n=len(nums)
        dp=[[float('-inf')]*2 for _ in range(n)]
        dp[0][0]=nums[0]
        dp[0][1]=0
        for i,num in enumerate(nums[1:],start=1):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+num)
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-num)
        return max(dp[-1])


if __name__ == '__main__':
    nums = [4, 2, 5, 3]
    print(Solution().maxAlternatingSum(nums))