"""
525. 连续数组
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

 

示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contiguous-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        思路：如果需要计算01匹配时，可将0作为-1来计算，这样相同个1和0得到的结果为0
        @param nums:
        @return:
        """
        cnt = 0
        dic = {0: -1}
        res = 0
        for i, num in enumerate(nums):
            cnt += 1 if num == 1 else -1
            if cnt in dic:
                res = max(res, i - dic[cnt])
            else:
                dic[cnt] = i
        return res


if __name__ == '__main__':
    nums = [0, 1]
    print(Solution().findMaxLength(nums))
