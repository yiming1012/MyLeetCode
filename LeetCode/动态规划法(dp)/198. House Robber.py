'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了37.62%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了5.79%的用户
        :param nums:
        :return:
        '''
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums.insert(0, 0)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

    def rob2(self, nums: List[int]) -> int:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了73.07%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.79%的用户
        :param nums:
        :return:
        '''
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        a = nums[0]
        b = max(a, nums[1])
        for i in range(2, len(nums)):
            b, a = max(a + nums[i], b), b
        return b

    def rob3(self, nums: List[int]) -> int:
        """
        执行用时 :44 ms, 在所有 Python3 提交中击败了37.62%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.79%的用户
        思路：因为迭代时，需要用到前面两项的值，所以用a,b表示，而不是数组，使得空间复杂度为O(1)
        时间复杂度：O(N)
        空间复杂度：O(1)
        :param nums:
        :return:
        """

        a, b = 0, 0
        for num in nums:
            a, b = b, max(b, a + num)
        return b


'''
上面三步为优化的过程：
状态转移方程：dp[i]=max(dp[i-2]+nums[i],dp[i-1])
'''

if __name__ == '__main__':
    nums = [2, 1, 3, 4, 3]
    s = Solution()
    print(s.rob3(nums))
