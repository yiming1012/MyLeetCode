"""
738. 单调递增的数字
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
说明: N 是在 [0, 10^9] 范围内的一个整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/monotone-increasing-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """
        思路：
        1. 找到第一个前面字符大于后面字符的位置
        2 从后往前判断，前面大的字符减一后，是否不小于前面的字符
        @param N:
        @return:
        """
        arr = list(str(N))
        n = len(arr)
        i = 0
        while i < n - 1 and arr[i] <= arr[i + 1]:
            i += 1
        if i == n - 1: return N
        while i >= 0 and arr[i] > arr[i + 1]:
            arr[i] = str(int(arr[i]) - 1)
            i -= 1
        i += 2
        while i < n:
            arr[i] = '9'
            i += 1
        return int("".join(arr))


if __name__ == '__main__':
    N = 332
    print(Solution().monotoneIncreasingDigits(N))
