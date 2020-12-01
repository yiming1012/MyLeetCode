"""
5615. 使数组互补的最少操作次数
给你一个长度为 偶数 n 的整数数组 nums 和一个整数 limit 。每一次操作，你可以将 nums 中的任何整数替换为 1 到 limit 之间的另一个整数。

如果对于所有下标 i（下标从 0 开始），nums[i] + nums[n - 1 - i] 都等于同一个数，则数组 nums 是 互补的 。例如，数组 [1,2,3,4] 是互补的，因为对于所有下标 i ，nums[i] + nums[n - 1 - i] = 5 。

返回使数组 互补 的 最少 操作次数。

 

示例 1：

输入：nums = [1,2,4,3], limit = 4
输出：1
解释：经过 1 次操作，你可以将数组 nums 变成 [1,2,2,3]（加粗元素是变更的数字）：
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
对于每个 i ，nums[i] + nums[n-1-i] = 4 ，所以 nums 是互补的。
示例 2：

输入：nums = [1,2,2,1], limit = 2
输出：2
解释：经过 2 次操作，你可以将数组 nums 变成 [2,2,2,2] 。你不能将任何数字变更为 3 ，因为 3 > limit 。
示例 3：

输入：nums = [1,2,1,2], limit = 2
输出：0
解释：nums 已经是互补的。
 

提示：

n == nums.length
2 <= n <= 105
1 <= nums[i] <= limit <= 105
n 是偶数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-moves-to-make-array-complementary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # 看target落在哪个区间
        """
        若 sum in [x + 1, x + y - 1]sum∈[x+1,x+y−1]，则只需要修改一次
        若 sum in [x + y]sum∈[x+y]，则不需要修改
        若 sum in [x + y + 1, limit + y]sum∈[x+y+1,limit+y]，则只需要修改一次
        若 sum in [2, x]sum∈[2,x]，则需要修改两次
        若 sum in [limit + y + 1, 2 * limit]sum∈[limit+y+1,2∗limit]，则需要修改两次
        """
        diff = [0] * (2 * limit + 2)
        n = len(nums)
        for i in range(n // 2):
            l = nums[i]
            r = nums[n - i - 1]
            if l > r:
                l, r = r, l
            diff[l + 1] += 1
            diff[l + r] -= 1
            diff[l + r + 1] += 1
            diff[limit + r + 1] -= 1
            diff[2] += 2
            diff[l + 1] -= 2
            diff[limit + r + 1] += 2
            diff[2 * limit + 1] -= 2

        res = float('inf')
        for i in range(2, 2 * limit + 1):
            diff[i] += diff[i - 1]
            res = min(res, diff[i])
        return res


if __name__ == '__main__':
    nums = [1, 2, 4, 3]
    limit = 4
    print(Solution().minMoves(nums, limit))
