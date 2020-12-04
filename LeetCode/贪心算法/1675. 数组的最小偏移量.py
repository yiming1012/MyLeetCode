"""
1675. 数组的最小偏移量
给你一个由 n 个正整数组成的数组 nums 。

你可以对数组的任意元素执行任意次数的两类操作：

如果元素是 偶数 ，除以 2
例如，如果数组是 [1,2,3,4] ，那么你可以对最后一个元素执行此操作，使其变成 [1,2,3,2]
如果元素是 奇数 ，乘上 2
例如，如果数组是 [1,2,3,4] ，那么你可以对第一个元素执行此操作，使其变成 [2,2,3,4]
数组的 偏移量 是数组中任意两个元素之间的 最大差值 。

返回数组在执行某些操作之后可以拥有的 最小偏移量 。

 

示例 1：

输入：nums = [1,2,3,4]
输出：1
解释：你可以将数组转换为 [1,2,3,2]，然后转换成 [2,2,3,2]，偏移量是 3 - 2 = 1
示例 2：

输入：nums = [4,1,5,20,3]
输出：3
解释：两次操作后，你可以将数组转换为 [4,2,5,5,3]，偏移量是 5 - 2 = 3
示例 3：

输入：nums = [2,10,8]
输出：3
 

提示：

n == nums.length
2 <= n <= 105
1 <= nums[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimize-deviation-in-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq
from typing import List
from sortedcontainers import SortedList


class Solution:
    def minimumDeviation1(self, nums: List[int]) -> int:
        """
        思路：将所有数转化为偶数后，再不断除成奇数，同时比较最小值和最大值的差
        @param nums:
        @return:
        """
        nums = [-n * 2 if n & 1 else -n for n in nums]  # 取负数用作最大堆
        left = -max(nums)  # 记录当前所有数字的最小值
        heapq.heapify(nums)
        diff = -nums[0] - left  # 记录当前最小偏移量
        while ~nums[0] & 1:
            half = nums[0] // 2
            if -half < left:
                left = -half
            heapq.heapreplace(nums, half)
            diff = min(diff, -nums[0] - left)
        return diff

    def minimumDeviation2(self, nums: List[int]) -> int:
        nums = SortedList(num << 1 if num & 1 else num for num in nums)
        ans = nums[-1] - nums[0]
        while not nums[-1] & 1:
            nums.add(nums.pop() >> 1)
            ans = min(ans, nums[-1] - nums[0])
        return ans


if __name__ == '__main__':
    nums = [4, 1, 5, 20, 3]
    print(Solution().minimumDeviation1(nums))
    print(Solution().minimumDeviation2(nums))
