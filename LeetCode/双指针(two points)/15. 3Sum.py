'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
from typing import List


class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        arr = []
        # 暴力法
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        subArr = [nums[i], nums[j], nums[k]]
                        subArr.sort()
                        # print(subArr)
                        if subArr not in arr:
                            arr.append(subArr)
        return arr

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        '''
        执行用时 :860 ms, 在所有 Python3 提交中击败了82.09%的用户
        内存消耗 :16.1 MB, 在所有 Python3 提交中击败了77.93%的用户
        :param nums:
        :return:
        '''
        length = len(nums)
        if length < 3:
            return []
        arr = []
        nums.sort()

        if nums[0] > 0 or nums[-1] < 0:
            return []

        for i in range(length - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            low, high = i + 1, length - 1
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if sum == 0:
                    subArr = [nums[i], nums[low], nums[high]]
                    arr.append(subArr)
                    while high - 1 > low and nums[high] == nums[high - 1]:
                        high -= 1
                    while low + 1 < high and nums[low] == nums[low + 1]:
                        low += 1
                    low += 1
                    high -= 1
                elif sum > 0:
                    high -= 1
                else:
                    low += 1

        return arr

    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        """
        思路：双指针
        1. 首先对数组排序
        2. 固定第一个数，后面两个利用双指针来左右逼近；
        3. 注意优化：如果左边数+中间数的两倍大于0，退出，因为后面的数更大；如果左边数+右边数的两个小于0，左边数继续往右遍历
        3. 注意去重是关键；如果两个连续的数相同，下标继续移动
        时间复杂度：O(N**2) 击败90%
        """
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i + 1, n - 1
            if nums[left] * 2 > target:
                break
            if nums[right] * 2 < target:
                continue
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res


'''
遇到题目首先考虑边界值：
    1）三个数相加，所以len(nums)>=3
    2) 排序后，如果首相大于0，尾项小于0，肯定三数之和不能为0
1、方法一用了三层for循环，时间复杂度为O(n**3)，在LeetCode上超时
2、方法二用了双指针，
    1）第一个数下标为i，第二个数low=i+1,第三个数high=len(nums)-1.
    2）如果三者和sum>target，调整low和high的值，直到sum==target
优化：
1. 当排序后的数组，首位大于target或者末尾小于target，不存在三数之和为target。（或者说前三位和大于target或后三位小于target，不存在符合条件的三个数）
2. 如果存在重复的数组，如果nums[i]==nums[i-1],继续下一位。当已知一组数满足条件后，nums[low]==nums[low+1],则low+=1或nums[high]==nums[high-1]，则high-=1
'''
if __name__ == '__main__':
    arr = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum1(arr))
    print(s.threeSum2(arr))
    print(s.threeSum3(arr))
