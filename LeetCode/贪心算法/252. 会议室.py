"""
252. 会议室
给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，请你判断一个人是否能够参加这里面的全部会议。

 

示例 1：

输入：intervals = [[0,30],[5,10],[15,20]]
输出：false
示例 2：

输入：intervals = [[7,10],[2,4]]
输出：true
 

提示：

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        stack = []
        intervals.sort()
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
