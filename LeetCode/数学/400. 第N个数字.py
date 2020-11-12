"""
400. 第N个数字
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32位整数范围内 ( n < 231)。

示例 1:

输入:
3

输出:
3
示例 2:

输入:
11

输出:
0

说明:
第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nth-digit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        num = 1
        cnt = 1
        # 计算n在哪个区间
        while n > num * cnt * 9:
            n -= num * cnt * 9
            cnt += 1
            num *= 10
        # 计算目标数
        target = num + (n - 1) // cnt
        # 计算在目标数的第几位
        index = (n - 1) % cnt
        return str(target)[index]


if __name__ == '__main__':
    n = 222
    print(Solution().findNthDigit(n))
