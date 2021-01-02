"""
239. 滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

进阶：

你能在线性时间复杂度内解决此题吗？

 

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
import heapq
from typing import List


class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        """
        思路：小根堆
        @param nums:
        @param k:
        @return:
        """
        heap = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        res = [-heap[0][0]]

        for i in range(k, n):
            heapq.heappush(heap, (-nums[i], i))
            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """
        思路：单调队列实现滑动窗口
        1. 保证队列单调递减
        2. 队列存储当前k个数中值从大到小的下标
        3. 如果队头元素下标到当前下标的长度超过了k，
        @param nums:
        @param k:
        @return:
        """
        queue = collections.deque()
        n = len(nums)
        for i in range(k):
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            queue.append((nums[i], i))
        res = [queue[0][0]]
        for i in range(k, n):
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            queue.append((nums[i], i))
            while queue and queue[0][1] <= i - k:
                queue.popleft()
            res.append(queue[0][0])
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().maxSlidingWindow1(nums, k))
    print(Solution().maxSlidingWindow2(nums, k))