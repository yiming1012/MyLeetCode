"""
1696. 跳跃游戏 VI
给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。

一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1, i + k)] 包含 两个端点的任意位置。

你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。

请你返回你能得到的 最大得分 。

 

示例 1：

输入：nums = [1,-1,-2,4,-7,3], k = 2
输出：7
解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。
示例 2：

输入：nums = [10,-5,-2,4,0,3], k = 3
输出：17
解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。
示例 3：

输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
输出：0
 

提示：

 1 <= nums.length, k <= 105
-104 <= nums[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-vi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
        思路：单调队列优化dp
        1. 单调队列维护一个单调递减的序列，且queue[0]与当前位置的距离小于等于k
        @param nums:
        @param k:
        @return:
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        queue = collections.deque()
        queue.append((nums[0], 0))
        for i in range(1, n):
            while queue and queue[0][1] < i - k:
                queue.popleft()
            cur = queue[0][0] + nums[i]
            # 构造单调递减队列
            while queue and queue[-1][0] <= cur:
                queue.pop()
            queue.append((cur, i))

        return cur


if __name__ == '__main__':
    nums = [1, -1, -2, 4, -7, 3]
    k = 2
    print(Solution().maxResult(nums, k))
