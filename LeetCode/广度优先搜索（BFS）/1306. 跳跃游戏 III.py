"""
这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr[i]。

请你判断自己是否能够跳到对应元素值为 0 的 任一 下标处。

注意，不管是什么情况下，你都无法跳到数组之外。

 

示例 1：

输入：arr = [4,2,3,0,3,1,2], start = 5
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案：
下标 5 -> 下标 4 -> 下标 1 -> 下标 3
下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3
示例 2：

输入：arr = [4,2,3,0,3,1,2], start = 0
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案：
下标 0 -> 下标 4 -> 下标 1 -> 下标 3
示例 3：

输入：arr = [3,0,2,1,2], start = 2
输出：false
解释：无法到达值为 0 的下标 1 处。
 

提示：

1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        思路：BFS
        1. 队列中存放可以到达的地方
        2. 已经到达过的索引存入set集合中
        @param arr:
        @param start:
        @return:
        """
        queue = collections.deque()
        n = len(arr)
        visited = set()
        queue.append((start, arr[start]))
        while queue:
            index, num = queue.popleft()
            if num == 0:
                return True
            visited.add(index)
            if index - num >= 0 and index - num not in visited:
                queue.append((index - num, arr[index - num]))
            if index + num < n and index + num not in visited:
                queue.append((index + num, arr[index + num]))
        return False


if __name__ == '__main__':
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    print(Solution().canReach(arr, start))
