"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        思路：利用二分优化
        """
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                nums[i:] = nums[i:][::-1]
                # print(nums)
                l, r = i, n - 1
                while l < r:
                    mid = l + (r - l) // 2
                    if nums[mid] <= nums[i - 1]:
                        l = mid + 1
                    else:
                        r = mid
                # print(l,nums[l])
                nums[l], nums[i - 1] = nums[i - 1], nums[l]
                break
        else:
            nums[:] = nums[::-1]
        return nums


if __name__ == '__main__':
    nums = [8, 7, 3, 5, 4, 2, 1]
    print(Solution().nextPermutation(nums))
