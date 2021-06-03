"""
878. 第 N 个神奇数字
如果正整数可以被 A 或 B 整除，那么它是神奇的。

返回第 N 个神奇数字。由于答案可能非常大，返回它模 10^9 + 7 的结果。

 

示例 1：

输入：N = 1, A = 2, B = 3
输出：2
示例 2：

输入：N = 4, A = 2, B = 3
输出：6
示例 3：

输入：N = 5, A = 2, B = 4
输出：10
示例 4：

输入：N = 3, A = 6, B = 4
输出：8
 

提示：

1 <= N <= 10^9
2 <= A <= 40000
2 <= B <= 40000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nth-magical-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from math import gcd


class Solution:
    def nthMagicalNumber(self, N: int, a: int, b: int) -> int:
        mod = 10 ** 9 + 7

        # 判断n中能被a和b整除的数的个数是否>=N
        def check(n):
            return n // a + n // b - n // c >= N

        # c为a和b的最小公倍数
        c = a * b // gcd(a, b)
        if a > b:
            a, b = b, a
        # 确定上下界
        l, r = a * N // 2, a * N
        # 二分法查找
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r % mod


if __name__ == '__main__':
    N = 1
    A = 2
    B = 3
    print(Solution().nthMagicalNumber(N, A, B))
