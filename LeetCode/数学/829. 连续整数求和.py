"""
829. 连续整数求和
给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?

示例 1:

输入: 5
输出: 2
解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
示例 2:

输入: 9
输出: 3
解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
示例 3:

输入: 15
输出: 4
解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
说明: 1 <= N <= 10 ^ 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/consecutive-numbers-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from math import sqrt


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # N = (s + s + n -1)*n/2
        # 枚举等差数列长度
        res = 0
        L = int(sqrt(2 * N))
        for i in range(1, L + 1):
            if 2 * N % i == 0 and (2 * N // i + 1 - i) % 2 == 0:
                res += 1
        return res


if __name__ == '__main__':
    N = 10
    print(Solution().consecutiveNumbersSum(N))
