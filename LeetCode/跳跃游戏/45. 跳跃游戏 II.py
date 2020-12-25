"""
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        思路：贪心算法
        1. 每次记录当前可以跳到的最远位置，且当前这一步可以走的范围为上一步能走的最远距离
        @param nums:
        @return:
        """

        n = len(nums)
        if n == 1:
            return 0
        # cur:当前跳的活动范围
        # nex:下一跳的最远距离
        # step:到达最后位置的最少步数
        cur, nex, step = 0, 0, 0

        for i, num in enumerate(nums):
            if i > cur:
                cur = nex
                step += 1
            nex = max(nex, i + num)
            if nex >= n - 1:
                return step + 1


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution().jump(nums))
