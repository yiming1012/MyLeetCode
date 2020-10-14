"""
给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

示例:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);

// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/random-pick-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from random import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        """
        思路：蓄水池抽样
        1. 如果有三个数，第一个被选中的概率为1，第二个被选中的概率为1/2，第三个被选中的概率为1/3
            a. 如果最终选择的第一个，那么后面两个不会被选中，概率P(1)=1*(1/2)*(2/3)=1/3
            b. 如果最终选择的第二个，那么前面和后面两个不会被选中，概率P(1)=1*(1/2)*(2/3)=1/3
            c. 如果最终选择的第三个，那么前面两个不会被选中，概率P(1)=1*(1/2)*(1/3)=1/3
        2. 分析可知，概率均为1/3
        @param target:
        @return:
        """
        index = -1
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                if random.randint(0, count) == 0:
                    index = i
                count += 1
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
