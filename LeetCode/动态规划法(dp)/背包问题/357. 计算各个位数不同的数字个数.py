"""
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

示例:

输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-numbers-with-unique-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countNumbersWithUniqueDigits1(self, n: int) -> int:
        if n == 0:
            return 1
        n = min(n, 10)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 10
        pre = 9
        k = 9
        for i in range(2, n + 1):
            pre *= k
            k -= 1
            dp[i] = dp[i - 1] + pre
        return dp[-1]

    def countNumbersWithUniqueDigits2(self, n: int) -> int:
        """
        思路：动态规划+排列组合
        1. n=0时，个数为1
        2. n=1时，个数为10
        3. n=2时，数字包含两位时，第一位可选1~9中的数，第二位可选0~10中除去第一位的数，即9*9，再加上一位数字的情况10
        4. n=3时，数字包含三位时，第一位第一位可选1~9中的数，第二位可选0~9中除去第一位的数，第三位可选0~9中除去前两位后的数，即9*9*8，再加上一位和两位的情况
        @param n:
        @return:
        """
        if n == 0:
            return 1

        res = 10
        pre = 9
        k = 9

        for i in range(2, 1 + min(10, n)):
            pre *= k
            k -= 1
            res += pre
        return res


if __name__ == '__main__':
    n = 3
    print(Solution().countNumbersWithUniqueDigits(n))
