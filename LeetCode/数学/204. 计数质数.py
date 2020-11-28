"""
204. 计数质数
统计所有小于非负整数 n 的质数的数量。

 

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0
 

提示：

0 <= n <= 5 * 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countPrimes1(self, n: int) -> int:
        """
        思路：埃氏筛法
        @param n:
        @return:
        """
        res = 0
        prime = [True] * n

        for i in range(2, n):
            if prime[i]:
                res += 1
                j = 2 * i
                while j < n:
                    prime[j] = False
                    j += i
        return res

    def countPrimes2(self, n: int) -> int:
        """
        思路：线性筛法
        @param n:
        @return:
        """
        flag = [True] * n
        prime = []

        for i in range(2, n):
            if flag[i]:
                prime.append(i)
            j = 0
            while prime[j] * i < n:
                flag[prime[j] * i] = False
                if i % prime[j] == 0:
                    break
                j += 1
        return len(prime)


if __name__ == '__main__':
    n = 10
    print(Solution().countPrimes1(n))
    print(Solution().countPrimes2(n))
