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
from functools import reduce
from typing import List


class Solution:
    def findTargetSumWays1(self, nums: List[int], S: int) -> int:
        n = len(nums)
        res = 0

        def dfs(index, presum):
            if index == n:
                nonlocal res
                if presum == S:
                    res += 1
                return

            dfs(index + 1, presum + nums[index])
            dfs(index + 1, presum - nums[index])

        dfs(0, 0)
        return res

    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        """
        代码真漂亮
        1. dfs遍历所有可能结果，以当前位置 i 和当前总和 cur 为根节点，以下一位数字的加减为邻域扩散搜索
        2. 利用 d 构造记忆，以便剪枝（搜索过程中遇到相同位置和相同cur值时返回值应该相同）
        3. dfs中 d 参数传的是引用，所以只有第一次会采用默认值 {}
        @param nums:
        @param S:
        @return:
        """

        def dfs(cur, i, d={}):
            # print(d)
            if i < len(nums) and (i, cur) not in d:  # 搜索周围节点
                d[(i, cur)] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == S))

        return dfs(0, 0)

    def findTargetSumWays3(self, nums: List[int], S: int) -> int:
        """
        思路：记忆化递归
        1. memo[(i,pre)]代表：i位置总和为pre能够成S的次数
        @param nums:
        @param S:
        @return:
        """
        n = len(nums)
        memo = {}

        def dfs(i, pre):
            print(memo)
            if (i, pre) in memo:
                return memo[(i, pre)]
            if i == n:
                tmp = int(pre == S)
                memo[(i, pre)] = tmp
                return tmp

            memo[(i, pre)] = dfs(i + 1, pre + nums[i]) + dfs(i + 1, pre - nums[i])
            return memo[(i, pre)]

        return dfs(0, 0)

    def findTargetSumWays4(self, nums: List[int], S: int) -> int:
        """
        思路：01背包问题
        1. nums总和为sumN，有两部分构成：正数P和负数N
        2. P+N=
        @param nums:
        @param S:
        @return:
        """
        sumN = reduce(lambda x, y: x + y, nums)
        if S > sumN or (sumN + S) & 1:
            return 0
        target = (sumN + S) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    S = 3
    print(Solution().findTargetSumWays1(nums, S))
    print(Solution().findTargetSumWays2(nums, S))
    print(Solution().findTargetSumWays3(nums, S))
