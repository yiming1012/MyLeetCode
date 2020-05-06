'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        执行用时 :84 ms, 在所有 Python3 提交中击败了48.97%的用户
        内存消耗 :15.2 MB, 在所有 Python3 提交中击败了12.50%的用户
        :param nums:
        :return:
        '''
        n = len(nums)
        now, maxIndex, step = 0, 0, 0
        for i in range(n - 1):
            if i + nums[i] >= n - 1:
                step += 1
                break
            if i + nums[i] > maxIndex:
                maxIndex = i + nums[i]
            if i == now:
                step += 1
                now = maxIndex
        return step



    def jump2(self, nums: List[int]) -> int:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了99.82%的用户
        内存消耗 :15 MB, 在所有 Python3 提交中击败了12.50%的用户
        思路:
        1.如果某一个作为 起跳点 的格子可以跳跃的距离是 3，那么表示后面 3 个格子都可以作为 起跳点。
            11. 可以对每一个能作为 起跳点 的格子都尝试跳一次，把 能跳到最远的距离 不断更新。

        2.如果从这个 起跳点 起跳叫做第 1 次 跳跃，那么从后面 3 个格子起跳 都 可以叫做第 2 次 跳跃。

        3.所以，当一次 跳跃 结束时，从下一个格子开始，到现在 能跳到最远的距离，都 是下一次 跳跃 的 起跳点。
            31. 对每一次 跳跃 用 for 循环来模拟。
            32. 跳完一次之后，更新下一次 起跳点 的范围。
            33. 在新的范围内跳，更新 能跳到最远的距离。

        4.记录 跳跃 次数，如果跳到了终点，就得到了结果。


        :param nums:
        :return:
        '''
        n = len(nums)
        now, maxIndex, step = 0, 0, 0
        for i in range(n - 1):
            # if i+nums[i]>=n-1:
            #     step+=1
            #     break
            if i + nums[i] > maxIndex:
                maxIndex = i + nums[i]
            if i == now:
                step += 1
                now = maxIndex
        return step


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    s = Solution()
    print(s.jump2(nums))
