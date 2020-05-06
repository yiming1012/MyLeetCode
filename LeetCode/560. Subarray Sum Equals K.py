'''

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        执行用时 :140 ms, 在所有 Python3 提交中击败了43.94%的用户
        内存消耗 :16.1 MB, 在所有 Python3 提交中击败了5.45%的用户
        思路：
            1、累加每一个数，添加到dict中
            2、巧妙之处在于，dict[0]=1.因为count+=dict[cumsum-k]，当前n个和为k时，cumsum-k=0
        :param nums:
        :param k:
        :return:
        '''
        dic = collections.defaultdict(lambda: 0)
        dic[0] = 1
        cumsum, count = 0, 0
        for i in range(len(nums)):
            cumsum += nums[i]
            if cumsum - k in dic:
                count += dic[cumsum - k]
            dic[cumsum] += 1
        return count


if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 3
    s = Solution()
    print(s.subarraySum(nums, k))
