"""
5741. 最高建筑高度
在一座城市里，你需要建 n 栋新的建筑。这些新的建筑会从 1 到 n 编号排成一列。

这座城市对这些新建筑有一些规定：

每栋建筑的高度必须是一个非负整数。
第一栋建筑的高度 必须 是 0 。
任意两栋相邻建筑的高度差 不能超过  1 。
除此以外，某些建筑还有额外的最高高度限制。这些限制会以二维整数数组 restrictions 的形式给出，其中 restrictions[i] = [idi, maxHeighti] ，表示建筑 idi 的高度 不能超过 maxHeighti 。

题目保证每栋建筑在 restrictions 中 至多出现一次 ，同时建筑 1 不会 出现在 restrictions 中。

请你返回 最高 建筑能达到的 最高高度 。

 

示例 1：


输入：n = 5, restrictions = [[2,1],[4,1]]
输出：2
解释：上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,1,2] ，最高建筑的高度为 2 。
示例 2：


输入：n = 6, restrictions = []
输出：5
解释：上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,3,4,5] ，最高建筑的高度为 5 。
示例 3：


输入：n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
输出：5
解释：上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,3,3,4,4,5,4,3] ，最高建筑的高度为 5 。
 

提示：

2 <= n <= 10^9
0 <= restrictions.length <= min(n - 1, 105)
2 <= idi <= n
idi 是 唯一的 。
0 <= maxHeighti <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-building-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxBuilding1(self, n: int, restrictions: List[List[int]]) -> int:
        """
        思路：求山脉中的最大值
        1. (i,hi)与(j,hj)之间的最大高度：h=(hi+hj+j-i)//2
        2. 或者(j-i-abs(hj-hi))//2 + max(hi,hj)
        @param n:
        @param restrictions:
        @return:
        """
        r = restrictions
        # 增加限制 (1, 0)
        r.append([1, 0])
        r.sort()

        # 增加限制 (n, n-1)
        if r[-1][0] != n:
            r.append([n, n - 1])

        m = len(r)

        # 从左向右传递限制
        for i in range(1, m):
            r[i][1] = min(r[i][1], r[i - 1][1] + (r[i][0] - r[i - 1][0]))
        # 从右向左传递限制
        for i in range(m - 2, 0, -1):
            r[i][1] = min(r[i][1], r[i + 1][1] + (r[i + 1][0] - r[i][0]))

        ans = 0
        for i in range(m - 1):
            # 计算 r[i + 1][0] 和 r[i][0]之间的建筑的最大高度
            best = ((r[i + 1][0] - r[i][0]) + r[i][1] + r[i + 1][1]) // 2
            ans = max(ans, best)
        return ans

    def maxBuilding2(self, n, A):
        A.append([1, 0])
        A.sort()
        if A[-1][0] != n:
            A.append([n, float('inf')])
        k = len(A)
        res = 0
        for i in range(1, k):
            A[i][1] = min(A[i][1], A[i - 1][1] + A[i][0] - A[i - 1][0])
        for i in range(k - 2, -1, -1):
            A[i][1] = min(A[i][1], A[i + 1][1] + A[i + 1][0] - A[i][0])
        for i in range(1, k):
            x = A[i][0] - A[i - 1][0] - abs(A[i][1] - A[i - 1][1])
            res = max(res, x // 2 + max(A[i][1], A[i - 1][1]))
        return res


if __name__ == '__main__':
    n = 5
    restrictions = [[2, 1], [4, 1]]
    print(Solution().maxBuilding(n, restrictions))
