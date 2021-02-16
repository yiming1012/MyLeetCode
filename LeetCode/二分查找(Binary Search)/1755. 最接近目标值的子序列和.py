"""
1755. 最接近目标值的子序列和
给你一个整数数组 nums 和一个目标值 goal 。

你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal 。也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum - goal) 。

返回 abs(sum - goal) 可能的 最小值 。

注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。

 

示例 1：

输入：nums = [5,-7,3,5], goal = 6
输出：0
解释：选择整个数组作为选出的子序列，元素和为 6 。
子序列和与目标值相等，所以绝对差为 0 。
示例 2：

输入：nums = [7,-9,15,-2], goal = -5
输出：1
解释：选出子序列 [7,-9,-2] ，元素和为 -4 。
绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。
示例 3：

输入：nums = [1,2,3], goal = -7
输出：7
 

提示：

1 <= nums.length <= 40
-107 <= nums[i] <= 107
-109 <= goal <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closest-subsequence-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import itertools
import bisect
from typing import List


class Solution:
    def minAbsDifference1(self, nums: List[int], goal: int) -> int:
        # 二分法
        n = len(nums)

        # 返回 arr中 0个 到 len(arr)个 的 sum(组合)
        def getAllComp(arr: List[int]):
            r = set()
            for i in range(len(arr) + 1):
                r |= {sum(k) for k in itertools.combinations(arr, i)}
            return r

        left = sorted(getAllComp(nums[:n // 2]))
        right = sorted(getAllComp(nums[n // 2:]))

        res = abs(goal)  # 最大就是 一个都不选的时候。
        for num in left:
            # 二分找到最接近 goal - num 的位置， 差值最小的就在 前一个，或者该位置。
            i = bisect.bisect_left(right, goal - num)
            if i == len(right):
                res = min(res, abs(right[-1] + num - goal))
            elif i == 0:
                res = min(res, abs(right[0] + num - goal))
            else:
                res = min(res, abs(right[i] + num - goal), abs(right[i - 1] + num - goal))

        return res

    def minAbsDifference2(self, nums: List[int], goal: int) -> int:
        # 方法二：双指针
        def getsum(nums):
            n = len(nums)
            arr = set()
            for i in range(2 ** n):
                cnt = 0
                for j in range(n):
                    if i >> j & 1:
                        cnt += nums[j]
                arr |= {cnt}
            return list(arr)

        left = getsum(nums[:len(nums) // 2])
        right = getsum(nums[len(nums) // 2:])
        res = float('inf')
        left.sort()
        right.sort()

        l, r = 0, len(right) - 1
        while l < len(left) and r >= 0:

            res = min(res, abs(left[l] + right[r] - goal))
            if left[l] + right[r] > goal:
                r -= 1
            else:
                l += 1

        return res


if __name__ == '__main__':
    nums = [5, -7, 3, 5]
    goal = 6
    print(Solution().minAbsDifference1(nums, goal))
    print(Solution().minAbsDifference2(nums, goal))
