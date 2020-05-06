'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        '''
        执行用时 :1672 ms, 在所有 Python3 提交中击败了13.05%的用户
        内存消耗 :14.7 MB, 在所有 Python3 提交中击败了12.50%的用户
        第一遍的答案
        :param nums:
        :return:
        '''
        dic = collections.Counter(nums)
        maxValue = 0

        for i in dic:
            if dic[i] > maxValue:
                maxValue = dic[i]

        res = len(nums)

        for i in dic:
            if dic[i] == maxValue:
                index_left = nums.index(i)
                index_right = nums[::-1].index(i)
                length = len(nums) - (index_left + index_right)
                res = min(res, length)

        return res

    def findShortestSubArray2(self, nums: List[int]) -> int:
        '''
        执行用时 :260 ms, 在所有 Python3 提交中击败了93.81%的用户
        内存消耗 :14.9 MB, 在所有 Python3 提交中击败了12.50%的用户
        思路：
        1. 统计每个字符出现的次数，并获取最大值
        2. 遍历获取每个字符出现的首尾下标
        3.计算出现最多次数的字母首尾下标之差加1（即长度）的最小值
        :param nums:
        :return:
        '''
        count = collections.Counter(nums)
        maxNum = max(count.values())
        dic = collections.defaultdict(list)
        for i, num in enumerate(nums):
            if num not in dic:
                arr = [i, i]
                dic[num] = arr
            else:
                dic[num][1] = i
        # print(dic)
        res = len(nums)
        for i in dic:
            if count[i] == maxNum:
                res = min(res, dic[i][1] - dic[i][0] + 1)
        return res

    def findShortestSubArray3(self, nums: List[int]) -> int:
        '''
        题解区的答案 most_common应用
        :param nums:
        :return:
        '''
        degree, ans = -1, len(nums)
        for num, frequency in collections.Counter(nums).most_common():
            if degree == -1: degree = frequency
            if frequency != degree: return ans
            ans = min(ans, len(nums) - nums[::-1].index(num) - nums.index(num))
        return ans


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1]
    print(Solution().findShortestSubArray2(nums))
