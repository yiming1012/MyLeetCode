"""
编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
说明:

1 是任何给定 primes 的超级丑数。
 给定 primes 中的数字以升序排列。
0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000 。
第 n 个超级丑数确保在 32 位有符整数范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        思路：和丑数II类似，不过由原来的2,3,5变成了一个数组，实现方式类似
        1. 先找最小值，判断是哪个元素的第几个序列，对应索引+1即可
        @param n:
        @param primes:
        @return:
        """
        dp = [1] * n
        m = len(primes)
        index = [0] * m

        for i in range(1, n):
            dp[i] = min([dp[index[j]] * primes[j] for j in range(m)])

            for j in range(m):
                if dp[i] == dp[index[j]] * primes[j]:
                    index[j] += 1

        return dp[-1]

