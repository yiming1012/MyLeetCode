"""
539. 最小时间差
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

 

示例 1：

输入：timePoints = ["23:59","00:00"]
输出：1
示例 2：

输入：timePoints = ["00:00","23:59","00:00"]
输出：0
 

提示：

2 <= timePoints <= 2 * 104
timePoints[i] 格式为 "HH:MM"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-time-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        思路：
        1. 排序后，相邻两数之差
        2. 最大值与最小值可能很近
        @param timePoints:
        @return:
        """
        arr = []
        for time in timePoints:
            t = time.split(":")
            s = int(t[0]) * 60 + int(t[1])
            arr.append(s)
        arr.sort()

        diff = arr[0] + 24 * 60 - arr[-1]
        for i in range(len(arr) - 1):
            diff = min(diff, arr[i + 1] - arr[i])

        return diff

