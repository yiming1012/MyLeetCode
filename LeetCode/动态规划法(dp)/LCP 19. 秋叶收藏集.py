"""
小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

示例 1：

输入：leaves = "rrryyyrryyyrr"

输出：2

解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

示例 2：

输入：leaves = "ryr"

输出：0

解释：已符合要求，不需要额外操作

提示：

3 <= leaves.length <= 10^5
leaves 中只包含字符 'r' 和字符 'y'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/UlBDOe
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minimumOperations1(self, leaves: str) -> int:
        '''
        左端全部为【红】的最小花费.
        左端全部为【红，黄】的最小花费.
        左端全部为【红，黄，红】的最小花费.
        '''
        n = len(leaves)
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][0] = 1 if leaves[0] == "y" else 0

        for i in range(1, n):
            flag = int(leaves[i] == "y")
            dp[i][0] = dp[i - 1][0] + flag
            dp[i][1] = min(dp[i - 1][1], dp[i - 1][0]) + 1 - flag
            dp[i][2] = min(dp[i - 1][2], dp[i - 1][1]) + flag

        return dp[-1][2]

    def minimumOperations2(self, leaves: str) -> int:
        t, ma, ans = 0, None, 1e100
        for i, c in enumerate(leaves):
            if c == 'y':
                t += 1
            if i == len(leaves) - 1:
                break
            a = i - 2 * t
            # print(i, t, a, ma)
            if ma is not None:
                ans = min(ans, a - ma)
            if ma is None or ma < a:
                ma = a
        return ans + t

    def minimumOperations3(self, leaves: str) -> int:
        a, b, c = int(leaves[0] == 'y'), float('inf'), float('inf')
        for i in range(1, len(leaves)):
            x = int(leaves[i] == 'y')
            a, b, c = a + x, min(a, b) + (1 - x), min(b, c) + x
        return c


if __name__ == '__main__':
    leaves = "rrryyyrryyyrr"
    print(Solution().minimumOperations1(leaves))
    print(Solution().minimumOperations2(leaves))
    print(Solution().minimumOperations3(leaves))
