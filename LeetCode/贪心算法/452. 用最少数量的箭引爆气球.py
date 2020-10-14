"""
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。

一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

Example:

输入:
[[10,16], [2,8], [1,6], [7,12]]

输出:
2

解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        思路：贪心算法
        1. 按照起点从小到大排序，如果新的区间的起点ll小于当前区间的终点r，就缩小区间r = min(r, rr)，令r等于当前区间和新区间终点的最小值
        2. 如果新区间的起点ll大于当前区间的终点，则需要新的箭，res+1,同时设置新的区间的终点r
        @param points:
        @return:
        """
        if not points:
            return 0
        points.sort()
        res = 1
        l, r = points[0]
        for i in range(1, len(points)):
            ll, rr = points[i]
            if ll > r:
                res += 1
                r = rr
            else:
                r = min(r, rr)
        return res

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        """
        思路：贪心算法
        1. 与思路1类似，该方法对每个区间的右端点排序，判断下一个区间的左端点是否大于当前区间的右端点
        @param points:
        @return:
        """
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        res = 1
        l, r = points[0]
        for i in range(1, len(points)):
            ll, rr = points[i]
            if ll > r:
                res += 1
                r = rr

        return res


if __name__ == '__main__':
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(Solution().findMinArrowShots(points))
