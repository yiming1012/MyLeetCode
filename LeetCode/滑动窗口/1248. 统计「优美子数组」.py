"""
1248. 统计「优美子数组」
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def numberOfSubarrays1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        arr = [i for i in range(n) if nums[i] & 1]
        print(arr)
        m = len(arr)
        if m < k:
            return 0
        left = -1
        res = 0
        queue = collections.deque(arr[:k - 1])

        for i in range(k - 1, m):
            queue.append(arr[i])
            if i < m - 1:
                res += (queue[0] - left) * (arr[i + 1] - arr[i])
                print(res)
                left = queue.popleft()
            elif i == m - 1:
                res += (queue[0] - left) * (n - arr[i])

        return res

    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        """
        思路：前缀和+差分
        @param nums:
        @param k:
        @return:
        """
        dic = collections.defaultdict(lambda: 0)
        cumsum, res = 0, 0
        dic[0] = 1
        for i in range(len(nums)):
            cumsum += nums[i] & 1
            if cumsum - k in dic:
                res += dic[cumsum - k]
            dic[cumsum] += 1
        return res


if __name__ == '__main__':
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(Solution().numberOfSubarrays1(nums, k))
    print(Solution().numberOfSubarrays2(nums, k))
