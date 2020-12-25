"""
1318. 或运算的最小翻转次数
给你三个正整数 a、b 和 c。

你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算   a OR b == c  成立的最小翻转次数。

「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。

 

示例 1：



输入：a = 2, b = 6, c = 5
输出：3
解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c
示例 2：

输入：a = 4, b = 2, c = 7
输出：1
示例 3：

输入：a = 1, b = 2, c = 3
输出：0
 

提示：

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-flips-to-make-a-or-b-equal-to-c
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        思路：位运算
        1. x为 a|b
        2. z为x^c
        3. 如果z的某一位为1，则需要判断a,b,c了
            1. 如果c的当前位为1，说明a,b的当前位都为0，则只需将其中一个修改为1即可
            2. 如果c的当前位为0，说明a,b的当前位至少有一个为1，统计为1的个数即可，res += (a >> i & 1) + (b >> i & 1)
        @param a:
        @param b:
        @param c:
        @return:
        """
        x = a | b
        z = x ^ c
        res = 0
        for i in range(32):
            if z >> i & 1:
                if c >> i & 1:
                    res += 1
                else:
                    res += (a >> i & 1) + (b >> i & 1)
        return res


if __name__ == '__main__':
    a = 2
    b = 6
    c = 5
    print(Solution().minFlips(a, b, c))
