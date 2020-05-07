'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import time

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        执行用时 :9084 ms, 在所有 Python3 提交中击败了5.24%的用户
        内存消耗 :15.8 MB, 在所有 Python3 提交中击败了6.90%的用户
        :param nums:
        :return:
        '''
        n = len(nums)
        # dp记录当前最大可以跳到几
        dp = [0]
        for i, num in enumerate(nums):
            if i <= max(dp):
                if i + num >= n - 1:
                    return True
                else:
                    dp.append(i + num)
        return False

    def canJump2(self, nums: List[int]) -> bool:
        '''
        执行用时 :56 ms, 在所有 Python3 提交中击败了67.69%的用户
        内存消耗 :14.9 MB, 在所有 Python3 提交中击败了17.24%的用户
        思路：查看前面可到达的最大值maxIndex是否大于此时的index，然后比较max(index+num,maxIndex)
        :param nums:
        :return:
        '''
        n = len(nums)
        maxIndex = 0
        for i, num in enumerate(nums):
            if i <= maxIndex:
                maxIndex = max(i + num, maxIndex)
                if maxIndex >= n - 1:
                    return True
        return False


    def canJump3(self, nums: List[int]) -> bool:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了96.52%的用户
        内存消耗 :15.1 MB, 在所有 Python3 提交中击败了6.90%的用户
        思路：倒序，每次记录
        :param nums:
        :return:
        '''
        if len(nums) <= 1:
            return True
        last_point = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_point:
                last_point = i
        return last_point == 0


if __name__ == '__main__':
    startTime=time.time()
    nums = [2, 3, 1, 1, 4]
    s = Solution()
    print(s.canJump(nums))
    endTime = time.time()
    print(endTime-startTime)
