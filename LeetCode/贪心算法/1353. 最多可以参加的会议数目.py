"""
1353. 最多可以参加的会议数目
给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 endDayi 。

你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。注意，一天只能参加一个会议。

请你返回你可以参加的 最大 会议数目。



示例 1：



输入：events = [[1,2],[2,3],[3,4]]
输出：3
解释：你可以参加所有的三个会议。
安排会议的一种方案如上图。
第 1 天参加第一个会议。
第 2 天参加第二个会议。
第 3 天参加第三个会议。
示例 2：

输入：events= [[1,2],[2,3],[3,4],[1,2]]
输出：4
示例 3：

输入：events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
输出：4
示例 4：

输入：events = [[1,100000]]
输出：1
示例 5：

输入：events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
输出：7


提示：

1 <= events.length <= 10^5
events[i].length == 2
1 <= events[i][0] <= events[i][1] <= 10^5
"""
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        思路：贪心算法
        1. 线性扫描
        @param events:
        @return:
        """
        N = 10 ** 5 + 1
        events.sort(reverse=True)
        heap = []
        res = 0
        for i in range(1, N):
            while events and events[-1][0] == i:
                heapq.heappush(heap, events.pop()[1])
            while heap and heap[0] < i:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                res += 1
        return res


if __name__ == '__main__':
    events = [[1, 2], [2, 3], [3, 4], [1, 2]]
    print(Solution().maxEvents(events))
