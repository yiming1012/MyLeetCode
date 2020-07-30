"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

 

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
 

提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findTargetSumWays1(self, nums: List[int], S: int) -> int:
        """
        超时
        """
        print(nums)
        n = len(nums)
        cnt = []
        res = 0

        def dfs(index, presum, arr):
            nonlocal res
            if index == n:
                if presum == S:
                    res += 1
                cnt.append(arr.copy())
                return

            for j in [-1, 1]:
                dfs(index + 1, presum + j * nums[index], arr + [j * nums[index]])

        dfs(0, 0, [])
        print(cnt)
        return res

    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        """
        记忆化递归
        """
        n = len(nums)
        if n == 0:
            return 0
        dic = {}

        def dfs(i, total_sum):
            if i == n:
                if total_sum == S:
                    return 1
                else:
                    return 0
            if (i, total_sum) in dic:
                return dic[(i, total_sum)]
            res = dfs(i + 1, total_sum + nums[i]) + dfs(i + 1, total_sum - nums[i])
            dic[(i, total_sum)] = res
            return res

        return dfs(0, 0)


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    S = 3
    print(Solution().findTargetSumWays1(nums, S))
    print(Solution().findTargetSumWays2(nums, S))
