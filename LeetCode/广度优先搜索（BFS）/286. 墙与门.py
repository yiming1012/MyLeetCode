"""
286. 墙与门
你被给定一个 m × n 的二维网格 rooms ，网格中有以下三种可能的初始化值：

-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近门的距离 ，如果无法到达门，则填 INF 即可。

 

示例 1：


输入：rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
输出：[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
示例 2：

输入：rooms = [[-1]]
输出：[[-1]]
示例 3：

输入：rooms = [[2147483647]]
输出：[[2147483647]]
示例 4：

输入：rooms = [[0]]
输出：[[0]]
 

提示：

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] 是 -1、0 或 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/walls-and-gates
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = collections.deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        step = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) in visited: continue
                visited.add((x, y))
                rooms[x][y] = step
                for dx, dy in pos:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in visited and rooms[xx][yy] == 2147483647:
                        queue.append((xx, yy))
            step += 1


from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sorted_set = SortedSet()

        for i in range(len(nums)):
            num = nums[i]
            print(sorted_set)
            # find the successor of current element
            if sorted_set and sorted_set.bisect_left(num) < len(sorted_set):
                if sorted_set[sorted_set.bisect_left(num)] <= num + t:
                    return True

            # find the predecessor of current element
            if sorted_set and sorted_set.bisect_left(num) != 0:
                if num <= sorted_set[sorted_set.bisect_left(num) - 1] + t:
                    return True

            sorted_set.add(num)
            if len(sorted_set) > k:
                sorted_set.remove(nums[i - k])

        return False



