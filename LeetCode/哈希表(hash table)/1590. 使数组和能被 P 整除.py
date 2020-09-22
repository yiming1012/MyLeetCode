"""
给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。

请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。

子数组 定义为原数组中连续的一组元素。

 

示例 1：

输入：nums = [3,1,4,2], p = 6
输出：1
解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。
示例 2：

输入：nums = [6,3,5,2], p = 9
输出：2
解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。
示例 3：

输入：nums = [1,2,3], p = 3
输出：0
解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。
示例  4：

输入：nums = [1,2,3], p = 7
输出：-1
解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。
示例 5：

输入：nums = [1000000000,1000000000,1000000000], p = 3
输出：0
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/make-sum-divisible-by-p
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        思路：前缀和+哈希
        1. 先计算数组元素总和s和s%p的余数k
        2. 如果s<p，无法满足条件；如果k==0，说明不用删除已经满足条件
        3. 求前缀和pre，如果(pre-k+p)%p在字典dic中，说明存在可删除的子数组，并计算长度
        4. 利用字典dic存储当前前缀和的余数pre%p

        @param nums:
        @param p:
        @return:
        """
        n = len(nums)
        s = sum(nums)
        if s < p:
            return -1
        k = s % p
        if k == 0:
            return 0
        dic = {0: -1}
        pre = 0
        res = n
        for i, num in enumerate(nums):
            pre += num
            if (pre - k + p) % p in dic:
                res = min(res, i - dic[(pre - k + p) % p])
            dic[pre % p] = i

        return res if res != n else -1


if __name__ == '__main__':
    nums = [3, 1, 4, 2]
    p = 6
    print(Solution().minSubarray(nums, p))
