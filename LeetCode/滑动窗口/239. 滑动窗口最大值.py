"""
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
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        思路：单调队列实现滑动窗口
        1. 保证队列单调递减
        2. 队列存储当前k个数中值从大到小的下标
        3. 如果队头元素下标到当前下标的长度超过了k，
        @param nums:
        @param k:
        @return:
        """
        n = len(nums)
        if n == 0:
            return []
        queue = collections.deque()
        res = []
        for i in range(n):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)
            if queue[0] == i - k:
                queue.popleft()
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res


