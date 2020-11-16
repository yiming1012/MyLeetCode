"""
5602. 将 x 减到 0 的最小操作数
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。

如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。



示例 1：

输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
示例 2：

输入：nums = [5,6,7,8,9], x = 4
输出：-1
示例 3：

输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        思路：前缀和+哈希
        1. 从左至右计算前缀和
        2. 从右至左计算后缀和，并将每个值存入哈希
        3. 遍历前缀和pre，并查找x-pre在哈希中是否存在，记录最短距离即可
        @param nums:
        @param x:
        @return:
        """
        n = len(nums)
        if sum(nums) < x:
            return -1
        if sum(nums) == x:
            return n

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        sub = 0
        dic = {0: 0}
        for i, num in enumerate(nums[::-1]):
            sub += num
            dic[sub] = i + 1

        res = float('inf')
        for i in range(n + 1):
            if pre[i] > x:
                break
            if x - pre[i] in dic:
                res = min(res, i + dic[x - pre[i]])
        return res if res != float('inf') else -1


if __name__ == '__main__':
    nums = [1, 1, 4, 2, 3]
    x = 5
    print(Solution().minOperations(nums, x))
