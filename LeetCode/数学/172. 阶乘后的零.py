"""

给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        2*5时才会出现0
        10也会出现0
        所以只需要找出5出现的次数即可
        1*5 2*5 3*5 4*5 5*5 6*5 7*5 8*5 9*5 10*5
        以上是出现5的个数为10个，10个中还有5和10两个，总数为50//5+(50//5)//5=12
        """
        if n < 5:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)


if __name__ == '__main__':
    n = 50
    print(Solution().trailingZeroes(n))
