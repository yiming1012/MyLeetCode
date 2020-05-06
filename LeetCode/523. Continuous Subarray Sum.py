'''
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/continuous-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        执行用时 :1040 ms, 在所有 Python3 提交中击败了37.26%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了6.00%的用户
        思路：
        1、利用到前缀和
        2、查找数组中[j,i] ,(j<i-1)是否满足条件
        3、注意k=0的情况
        :param nums:
        :param k:
        :return:
        '''
        nums.insert(0, 0)
        for i in range(2, len(nums)):
            nums[i] += nums[i - 1]
            for j in range(i - 1):
                if (k == 0 and nums[i] == nums[j]) or (k != 0 and (nums[i] - nums[j]) % k == 0):
                    return True
        return False

    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        '''
        执行用时 :316 ms, 在所有 Python3 提交中击败了63.94%的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了6.00%的用户
        思路：对k取余数，如果前i-2个树中存在本次的值，则True
        :param nums:
        :param k:
        :return:
        '''
        nums.insert(0, 0)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            nums[i] = nums[i] % k if k != 0 else nums[i]
            if nums[i] in nums[:i - 1]:
                return True
        return False


    def checkSubarraySum3(self, nums: List[int], k: int) -> bool:
        '''
        官方解题
        :param nums:
        :param k:
        :return:
        '''
        sumdict = {}
        sumN = 0
        sumdict[0] = -1
        for i in range(len(nums)):
            sumN += nums[i]
            if k != 0: sumN = sumN % k
            if sumN in sumdict:
                if i - sumdict[sumN] > 1:
                    return True
            else:
                sumdict[sumN] = i
        return False


if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 3
    s = Solution()
    print(s.checkSubarraySum(nums, k))
