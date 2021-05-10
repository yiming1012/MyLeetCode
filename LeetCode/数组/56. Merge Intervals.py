'''
56. 合并区间
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        执行用时 :56 ms, 在所有 Python3 提交中击败了66.07%的用户
        内存消耗 :14.6 MB, 在所有 Python3 提交中击败了62.50%的用户
        思路：合并区间，一般都需要先排序，只需要比较后面的第一位和前面的后一位就行。
        1、如果新的数组，第一位比前一数组的后一位大，说明可以合并，并获取
        :param intervals:
        :return:
        '''
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        # print(intervals)
        res = list()
        res.append(intervals[0])
        for num in intervals[1:]:
            if num[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], num[1])
            else:
                res.append(num)
        # print(res)
        return res

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        执行用时 :72 ms, 在所有 Python3 提交中击败了48.09%的用户
        内存消耗 :14.2 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：不使用额外的空间
        :param intervals:
        :return:
        '''
        intervals.sort()
        i = 1
        while i < len(intervals):
            a = intervals[i - 1]
            b = intervals[i]
            if b[0] <= a[1]:
                intervals[i - 1][1] = max(a[1], b[1])
                intervals.pop(i)
            else:
                i += 1
        return intervals


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了97.72%的用户
        内存消耗 :14.6 MB, 在所有 Python3 提交中击败了75.00%的用户
        :param intervals:
        :return:
        '''
        if len(intervals) == 0:
            return []

        intervals.sort()
        result = [intervals[0]]

        high = intervals[0][1]
        for i in range(1, len(intervals)):
            if high < intervals[i][0]:
                result.append(intervals[i])
                high = intervals[i][1]
            elif intervals[i][0] <= high <= intervals[i][1]:
                result[-1][1] = intervals[i][1]
                high = intervals[i][1]
            elif intervals[i][1] < high:
                continue

        return result

    def merge4(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 16], [15, 18]]
    s = Solution()
    print(s.merge(intervals))
