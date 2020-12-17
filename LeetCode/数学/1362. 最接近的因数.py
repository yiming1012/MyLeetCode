"""
1362. 最接近的因数
给你一个整数 num，请你找出同时满足下面全部要求的两个整数：

两数乘积等于  num + 1 或 num + 2
以绝对差进行度量，两数大小最接近
你可以按任意顺序返回这两个整数。



示例 1：

输入：num = 8
输出：[3,3]
解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 & 3 。
示例 2：

输入：num = 123
输出：[5,25]
示例 3：

输入：num = 999
输出：[40,25]


提示：

1 <= num <= 10^9
"""
from math import sqrt
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        res = [-1, -1]

        def check(target):
            n = int(sqrt(target)) + 1
            for i in range(1, n):
                if target % i == 0:
                    second = target // i
                    if res[0] == -1 or (abs(res[0] - res[1]) > abs(i - second)):
                        res[0] = i
                        res[1] = second

        check(num + 1)
        check(num + 2)
        return res


if __name__ == '__main__':
    num = 10
    print(Solution().closestDivisors(num))
