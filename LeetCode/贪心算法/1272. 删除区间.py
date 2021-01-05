"""
1272. 删除区间
给你一个 有序的 不相交区间列表 intervals 和一个要删除的区间 toBeRemoved， intervals 中的每一个区间 intervals[i] = [a, b]
都表示满足 a <= x < b 的所有实数  x 的集合。

我们将 intervals 中任意区间与 toBeRemoved 有交集的部分都删除。

返回删除所有交集区间后， intervals 剩余部分的 有序 列表。



示例 1：

输入：intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
输出：[[0,1],[6,7]]
示例 2：

输入：intervals = [[0,5]], toBeRemoved = [2,3]
输出：[[0,2],[3,5]]


提示：

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9
"""
from typing import List



class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        """
        思路：
        1. 先判断没有交集的情况 r <= L or l >= R
        2. 剩下的情况则是会有交集的，在判断左边和右边超出toBeRemoved的区间
        @param intervals:
        @param toBeRemoved:
        @return:
        """
        L, R = toBeRemoved
        res = []
        for l, r in intervals:
            if r <= L or l >= R:
                res.append([l, r])
            else:
                if l < L:
                    res.append([l, L])
                if r > R:
                    res.append([R, r])
        return res


if __name__ == '__main__':
    intervals = [[0, 2], [3, 4], [5, 7]]
    toBeRemoved = [1, 6]
    print(Solution().removeInterval(intervals, toBeRemoved))
