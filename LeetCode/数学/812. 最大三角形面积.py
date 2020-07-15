"""
给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

示例:
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释:
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。


注意:

3 <= points.length <= 50.
不存在重复的点。
 -50 <= points[i][j] <= 50.
结果误差值在 10^-6 以内都认为是正确答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-triangle-area
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        思路：鞋带公式

        """

        n = len(points)
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    res = max(res,
                              abs(points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[i][1]
                              - points[i][1] * points[j][0] - points[j][1] * points[k][0] - points[k][1] * points[i][0])/2)
        return res


if __name__ == '__main__':
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print(Solution().largestTriangleArea(points))
