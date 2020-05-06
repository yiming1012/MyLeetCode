'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from itertools import accumulate
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        执行用时 :64 ms, 在所有 Python3 提交中击败了40.17%的用户
        内存消耗 :14 MB, 在所有 Python3 提交中击败了5.04%的用户
        思路：利用栈存储已经经过的点，用遇到更大的就计算
        1、后一个数比前一个数大才计算，比前一个数小继续入栈
        2、维护一个单调递减的stack
        :param height:
        :return:
        '''

        def fun(height, res):
            if len(height) <= 1:
                return res
            stack = []
            index = 0
            stack.append(height[0])
            for i in range(1, len(height)):
                if height[i] >= height[index]:
                    square = (i - index) * height[index]
                    res += square
                    while len(stack) > 0:
                        res -= stack.pop()
                    index = i
                stack.append(height[i])

            if len(stack) > 0:
                stack.reverse()
                res = fun(stack, res)
            return res

        return fun(height, 0)

    def trap2(self, height: List[int]) -> int:
        stack = []  # (height, index)
        n = len(height)
        res = 0
        for i in range(n):
            while stack and height[i] >= stack[-1][0]:
                cur = stack.pop()
                if not stack: break
                currentHeight = min(height[i], stack[-1][0]) - cur[0]
                res += currentHeight * (i - stack[-1][1] - 1)
            stack.append((height[i], i))
        return res

    def trap3(self, height: List[int]) -> int:
        '''
        执行用时 :60 ms, 在所有 Python3 提交中击败了49.49%的用户
        内存消耗 :14.2 MB, 在所有 Python3 提交中击败了5.04%的用户
        思路：单调栈
        :param height:
        :return:
        '''
        stack = []
        n = len(height)
        res = 0
        for i in range(n):
            while stack and height[i] >= height[stack[-1]]:
                index = stack.pop()
                if not stack:
                    break
                minHeight = min(height[i], height[stack[-1]]) - height[index]
                res += minHeight * (i - stack[-1] - 1)
            stack.append(i)

        return res

    def trap4(self, height: List[int]) -> int:
        return sum(map(min, accumulate(height, max), list(accumulate(height[::-1], max))[::-1])) - sum(height)

    def trap5(self, height: List[int]) -> int:
        '''
        执行用时 :72 ms, 在所有 Python3 提交中击败了28.11%的用户
        内存消耗 :14 MB, 在所有 Python3 提交中击败了5.04%的用户
        思路：动态规划法
        :param height:
        :return:
        '''
        n = len(height)
        leftArr = [0] * n
        rightArr = [0] * n
        left_max = 0
        right_max = 0

        for i in range(n):
            left_max = max(left_max, height[i])
            leftArr[i] = left_max

        for i in range(n - 1, -1, -1):
            right_max = max(right_max, height[i])
            rightArr[i] = right_max

        res = 0
        for i in range(n):
            res += min(leftArr[i], rightArr[i]) - height[i]

        return res

    """
    双指针法真的妙，那么如何理解双指针法呢？听我来给你捋一捋。（捋的过程和原解中的C++在细节方面的处理是有出入的）
    
    我们先明确几个变量的意思：
    
    left_max：左边的最大值，它是从左往右遍历找到的
    right_max：右边的最大值，它是从右往左遍历找到的
    left：从左往右处理的当前下标
    right：从右往左处理的当前下标
    定理一：在某个位置i处，它能存的水，取决于它左右两边的最大值中较小的一个。
    
    定理二：当我们从左往右处理到left下标时，左边的最大值left_max对它而言是可信的，但right_max对它而言是不可信的。（见下图，由于中间状况未知，对于left下标而言，right_max未必就是它右边最大的值）
    
    定理三：当我们从右往左处理到right下标时，右边的最大值right_max对它而言是可信的，但left_max对它而言是不可信的。
    
                                       right_max
     left_max                             __
       __                                |  |
      |  |__   __??????????????????????  |  |
    __|     |__|                       __|  |__
            left                      right
    对于位置left而言，它左边最大值一定是left_max，右边最大值“大于等于”right_max，这时候，如果left_max<right_max成立，那么它就知道自己能存多少水了。无论右边将来会不会出现更大的right_max，都不影响这个结果。 所以当left_max<right_max时，我们就希望去处理left下标，反之，我们希望去处理right下标。
    """

    def trap6(self, height: List[int]) -> int:
        '''
        执行用时 :60 ms, 在所有 Python3 提交中击败了49.49%的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.04%的用户
        思路：双指针
        :param height:
        :return:
        '''
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        ans = 0
        while left <= right:
            if left_max < right_max:
                ans += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                ans += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
        return ans


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    print(s.trap(height))
