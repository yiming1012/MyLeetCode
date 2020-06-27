"""
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def findDuplicates1(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                res.append(abs(num))
        return res

        # return [k for k,v in collections.Counter(nums).items() if v==2]

    def findDuplicates2(self, nums: List[int]) -> List[int]:
        return [k for k, v in collections.Counter(nums).items() if v == 2]

    def findDuplicates3(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, num in enumerate(nums):
            if num != i + 1:
                res.append(num)
        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    # print(Solution().findDuplicates1(nums))
    # print(Solution().findDuplicates2(nums))
    print(Solution().findDuplicates3(nums))
