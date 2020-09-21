"""
小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。请返回小扣共有多少种购买方案。

注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1

示例 1：

输入：staple = [10,20,5], drinks = [5,5,2], x = 15

输出：6

解释：小扣有 6 种购买方案，所选主食与所选饮料在数组中对应的下标分别是：
第 1 种方案：staple[0] + drinks[0] = 10 + 5 = 15；
第 2 种方案：staple[0] + drinks[1] = 10 + 5 = 15；
第 3 种方案：staple[0] + drinks[2] = 10 + 2 = 12；
第 4 种方案：staple[2] + drinks[0] = 5 + 5 = 10；
第 5 种方案：staple[2] + drinks[1] = 5 + 5 = 10；
第 6 种方案：staple[2] + drinks[2] = 5 + 2 = 7。

示例 2：

输入：staple = [2,1,1], drinks = [8,9,5,1], x = 9

输出：8

解释：小扣有 8 种购买方案，所选主食与所选饮料在数组中对应的下标分别是：
第 1 种方案：staple[0] + drinks[2] = 2 + 5 = 7；
第 2 种方案：staple[0] + drinks[3] = 2 + 1 = 3；
第 3 种方案：staple[1] + drinks[0] = 1 + 8 = 9；
第 4 种方案：staple[1] + drinks[2] = 1 + 5 = 6；
第 5 种方案：staple[1] + drinks[3] = 1 + 1 = 2；
第 6 种方案：staple[2] + drinks[0] = 1 + 8 = 9；
第 7 种方案：staple[2] + drinks[2] = 1 + 5 = 6；
第 8 种方案：staple[2] + drinks[3] = 1 + 1 = 2；

提示：

1 <= staple.length <= 10^5
1 <= drinks.length <= 10^5
1 <= staple[i],drinks[i] <= 10^5
1 <= x <= 2*10^5
"""
from typing import List


class Solution:
    def breakfastNumber1(self, s: List[int], d: List[int], x: int) -> int:
        mod = 10 ** 9 + 7
        res = 0
        dp = [0] * (x + 1)
        for num in d:
            if x >= num:
                dp[num] += 1
        for i in range(1, x + 1):
            dp[i] += dp[i - 1]

        for num in s:
            if x >= num:
                res += dp[x - num]

        return res % mod

    def breakfastNumber2(self, s: List[int], d: List[int], x: int) -> int:
        mod = 10 ** 9 + 7
        s.sort()
        d.sort()
        res = 0
        i = len(d) - 1
        for a in s:
            while i >= 0 and a + d[i] > x:
                i -= 1
            res += i + 1
        return res % mod


if __name__ == '__main__':
    staple = [10, 20, 5]
    drinks = [5, 5, 2]
    x = 15
    print(Solution().breakfastNumber1(staple, drinks, x))
    print(Solution().breakfastNumber2(staple, drinks, x))
