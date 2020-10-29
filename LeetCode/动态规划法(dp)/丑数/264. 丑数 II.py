"""
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq


class Solution:
    def nthUglyNumber1(self, n: int) -> int:
        """
        思路：动态规划法+三指针
        @param n:
        @return:
        """
        dp = [1] * n
        a, b, c = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
            if dp[i] == dp[a] * 2:
                a += 1
            if dp[i] == dp[b] * 3:
                b += 1
            if dp[i] == dp[c] * 5:
                c += 1
        return dp[-1]

    def nthUglyNumber2(self, n: int) -> int:
        """
        思路：堆优化
        @param n:
        @return:
        """
        pq = [1]
        res = None
        visited = set()
        while n:
            res = heapq.heappop(pq)
            n -= 1
            for i in [2, 3, 5]:
                tmp = res * i
                if tmp not in visited:
                    visited.add(tmp)
                    heapq.heappush(pq, tmp)
        return res


if __name__ == '__main__':
    n = 100
    print(Solution().nthUglyNumber1(n))
    print(Solution().nthUglyNumber2(n))
