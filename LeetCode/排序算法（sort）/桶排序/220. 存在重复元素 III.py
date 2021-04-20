"""
220. 存在重复元素 III
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

如果存在则返回 true，不存在返回 false。

 

示例 1：

输入：nums = [1,2,3,1], k = 3, t = 0
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1, t = 2
输出：true
示例 3：

输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false
 

提示：

0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        st = SortedSet()

        for i in range(len(nums)):
            num = nums[i]
            index = st.bisect_left(num - t)
            print(st)
            if index < len(st) and st[index] <= num + t:
                return True

            st.add(num)
            if len(st) > k:
                st.remove(nums[i - k])

        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    print(Solution().containsNearbyAlmostDuplicate(nums, k, t))
