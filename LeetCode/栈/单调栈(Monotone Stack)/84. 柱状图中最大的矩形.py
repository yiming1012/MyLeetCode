"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 



以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

 



图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

 

示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        """
        思路：单调栈(Monotone Stack)
        时间复杂度：O(N)，输入数组里的每一个元素入栈一次，出栈一次。
        空间复杂度：O(N)，栈的空间最多为 NN。
                 ——
              —— ——
              —— ——
              —— ——    ——
        ——    —— —— —— ——
        —— —— —— —— —— ——
        1. 原始数组中首尾补充0
        2. 保持单调栈中的元素单调上升的，当遇到一个比栈顶元素小的数时，将栈顶元素弹出栈，并计算矩形面积
        3. 计算当前弹出的元素下标与栈顶下标的距离，乘上当前的高度
        4. 记录每次计算的最大值
        """
        stack = []
        res = 0
        # heights = [0] + heights + [0]
        heights.insert(0, 0)
        heights.append(0)
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                k = stack[-1] + 1
                res = max(res, (i - k) * h)
            stack.append(i)
        return res

    def largestRectangleArea2(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                right[index] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        res = 0
        for i in range(n):
            res = max(res, heights[i] * (right[i] - left[i] - 1))
        return res


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea1(heights))
    print(Solution().largestRectangleArea2(heights))
