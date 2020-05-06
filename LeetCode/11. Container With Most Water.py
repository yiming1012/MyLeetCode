'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        执行用时 :96 ms, 在所有 Python3 提交中击败了87.29%的用户
        内存消耗 :14.8 MB, 在所有 Python3 提交中击败了18.15%的用户
        :param height:
        :return:
        '''
        if len(height) < 2:
            return 0
        left, right, maxValue = 0, len(height) - 1, 0
        while left < right:
            s = min(height[left], height[right]) * (right - left)
            maxValue = max(maxValue, s)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxValue

    def maxArea2(self, height: List[int]) -> int:
        '''
        执行用时 :88 ms, 在所有 Python3 提交中击败了88.28%的用户
        内存消耗 :14.7 MB, 在所有 Python3 提交中击败了18.15%的用户
        :param height:
        :return:
        '''
        if len(height) < 2:
            return 0
        left, right, maxValue = 0, len(height) - 1, 0

        while left < right:
            leftValue = height[left]
            rightValue = height[right]
            s = min(leftValue, rightValue) * (right - left)
            maxValue = max(maxValue, s)
            if left < right and leftValue < rightValue:
                while height[left] <= leftValue:
                    left += 1
            else:

                while left < right and height[right] <= rightValue:
                    right -= 1

        return maxValue

'''
本题关键是：利用左右双指针向中间靠拢
'''