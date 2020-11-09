"""
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0

        def sort(nums):
            if len(nums) < 2:
                return nums
            mid = len(nums) // 2
            left = sort(nums[:mid])
            right = sort(nums[mid:])
            return merge(left, right)

        def merge(left, right):
            m, n = len(left), len(right)
            i, j = 0, 0
            # 计算满足条件的
            while i < m and j < n:
                if left[i] > 2 * right[j]:
                    j += 1
                    nonlocal res
                    res += m - i
                else:
                    i += 1

            # 归并排序
            i, j = 0, 0
            arr = []
            while i < m and j < n:
                if left[i] <= right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1

            if i < m:
                arr += left[i:]
            if j < n:
                arr += right[j:]
            return arr

        ans = sort(nums)
        return res


if __name__ == '__main__':
    nums = [1, 3, 2, 3, 1]
    print(Solution().reversePairs(nums))
