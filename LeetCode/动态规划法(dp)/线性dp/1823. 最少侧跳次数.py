"""
1823. 最少侧跳次数
给你一个长度为 n 的 3 跑道道路 ，它总共包含 n + 1 个 点 ，编号为 0 到 n 。一只青蛙从 0 号点第二条跑道 出发 ，它想要跳到点 n 处。然而道路上可能有一些障碍。

给你一个长度为 n + 1 的数组 obstacles ，其中 obstacles[i] （取值范围从 0 到 3）表示在点 i 处的 obstacles[i] 跑道上有一个障碍。如果 obstacles[i] == 0 ，那么点 i 处没有障碍。任何一个点的三条跑道中 最多有一个 障碍。

比方说，如果 obstacles[2] == 1 ，那么说明在点 2 处跑道 1 有障碍。
这只青蛙从点 i 跳到点 i + 1 且跑道不变的前提是点 i + 1 的同一跑道上没有障碍。为了躲避障碍，这只青蛙也可以在 同一个 点处 侧跳 到 另外一条 跑道（这两条跑道可以不相邻），但前提是跳过去的跑道该点处没有障碍。

比方说，这只青蛙可以从点 3 处的跑道 3 跳到点 3 处的跑道 1 。
这只青蛙从点 0 处跑道 2 出发，并想到达点 n 处的 任一跑道 ，请你返回 最少侧跳次数 。

注意：点 0 处和点 n 处的任一跑道都不会有障碍。

 

示例 1：


输入：obstacles = [0,1,2,3,0]
输出：2
解释：最优方案如上图箭头所示。总共有 2 次侧跳（红色箭头）。
注意，这只青蛙只有当侧跳时才可以跳过障碍（如上图点 2 处所示）。
示例 2：


输入：obstacles = [0,1,1,3,3,0]
输出：0
解释：跑道 2 没有任何障碍，所以不需要任何侧跳。
示例 3：


输入：obstacles = [0,2,1,0,3,0]
输出：2
解释：最优方案如上图所示。总共有 2 次侧跳。
 

提示：

obstacles.length == n + 1
1 <= n <= 5 * 105
0 <= obstacles[i] <= 3
obstacles[0] == obstacles[n] == 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-sideway-jumps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def minSideJumps1(self, obstacles: List[int]) -> int:
        """
        思路：动态规划法
        1. 如果当前位置不为障碍物，可以由前面转移过来或上下跳过来
        2. 转移顺序是先从左向右，后上下转移
        @param obstacles:
        @return:
        """
        n = len(obstacles)
        dp = [1, 0, 1]
        for i in range(1, n):
            arr = dp[:]
            for j in range(3):
                if obstacles[i] == j + 1:
                    arr[j] = float('inf')
            for j in range(3):
                if obstacles[i] != j + 1:
                    arr[j] = min(arr[j], min(arr) + 1)
            dp = arr[:]
        return min(dp)

    def minSideJumps2(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        m = 3
        ob = set([(i, o - 1) for i, o in enumerate(obstacles) if o > 0])
        pos = [(1, 0), (0, -1), (0, -2), (0, 1), (0, 2)]
        print(ob)
        queue = collections.deque()
        queue.append((0, 1, 0))
        visited = set()
        res = float('inf')
        while queue:
            x, y, step = queue.popleft()
            if x == n - 1:
                res = min(res, step)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in pos:
                xx, yy = x + dx, y + dy
                if 0 <= xx < n and 0 <= yy < m and (xx, yy) not in ob and (xx, yy) not in visited:
                    if dx == 0:
                        queue.append((xx, yy, step + 1))
                    else:
                        queue.append((xx, yy, step))

        return res if res != float('inf') else 0
