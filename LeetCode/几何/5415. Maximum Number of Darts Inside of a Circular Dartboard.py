"""
You have a very large square wall and a circular dartboard placed on the wall. You have been challenged to throw darts into the board blindfolded. Darts thrown at the wall are represented as an array of points on a 2D plane. 

Return the maximum number of points that are within or lie on any circular dartboard of radius r.

 

Example 1:



Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.
Example 2:



Input: points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).
Example 3:

Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
Output: 1
Example 4:

Input: points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
Output: 4
 

Constraints:

1 <= points.length <= 100
points[i].length == 2
-10^4 <= points[i][0], points[i][1] <= 10^4
1 <= r <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math
from typing import List


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        """
        思路：
        1、我们的热点分析，是计算每两点之间的欧氏距离
        2、计算每个点point对应的距离小于R的最多的点，认为是热点

        不足：
        1、 一个三角形可能三个点都在圆内，但是通过上面的算法，不在圆内

        改进：
        试想最优解的圆，是否可以通过挪动后至少包含两个点在圆上（不是圆内）。
        因此可以使用O(N^2)枚举任意两个点，根据半径计算出圆上包含该两点的圆所对应的圆心，
        然后在O(N)统计所包含的点数。这里多说一句，大部分情况下存在两个方向的圆心（特例为直径线段两端点），
        可以想象在最优囊括范围内任意挪动圆，圆上两点总会存在同一个方向上的圆心，因此不必两个方向的圆心都计算。
        时间复杂度为O(N^3)

        想象下墙上钉了若干钉子，然后你用一个圈去套这些钉子。如果你的圈只碰到了一个钉子，你的圈仍然是可以移动的；
        但如果圈碰到了两个钉子，就不能再任意移动了。实质是：已知圆上一点和半径，可以有无数个圆；
        但如果是已知圆上两点和半径，则最多有两个圆（当这两点之间的距离恰好等于直径时，只有一个圆）
        """
        def dis(x1, y1, x2, y2):
            return math.sqrt(float((x1 - x2) ** 2) + float((y1 - y2) ** 2))

        def get_circle(x1, y1, x2, y2, r):
            midx = (x1 + x2) / 2.0
            midy = (y1 + y2) / 2.0
            angle = math.atan2(float(y2 - y1), float(x2 - x1))
            d = math.sqrt(r ** 2 - dis(x1, y1, midx, midy) ** 2)
            cx = midx + d * math.sin(angle)
            cy = midy - d * math.cos(angle)
            return cx, cy

        r = float(r)
        l = len(points)
        res = 1
        for i in range(l):
            for j in range(i + 1, l):
                if dis(points[i][0], points[i][1], points[j][0], points[j][1]) > r * 2:
                    continue
                cx, cy = get_circle(points[i][0], points[i][1], points[j][0], points[j][1], r)
                count = 0
                # 计算在以（cx,cy）为圆心，r为半径的圆内的点个数
                for k in range(l):
                    if dis(cx, cy, points[k][0], points[k][1]) < r + 1e-8:
                        count += 1
                res = max(res, count)
        return res


if __name__ == '__main__':
    point = [[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]]
    R = 5
    print(Solution().numPoints(point, R))
