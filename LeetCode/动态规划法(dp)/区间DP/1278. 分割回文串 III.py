"""
1278. 分割回文串 III
给你一个由小写字母组成的字符串 s，和一个整数 k。

请你按下面的要求分割字符串：

首先，你可以将 s 中的部分字符修改为其他的小写英文字母。
接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。
请返回以这种方式分割字符串所需修改的最少字符数。

 

示例 1：

输入：s = "abc", k = 2
输出：1
解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。
示例 2：

输入：s = "aabbc", k = 3
输出：0
解释：你可以把字符串分割成 "aa"、"bb" 和 "c"，它们都是回文串。
示例 3：

输入：s = "leetcode", k = 8
输出：0
 

提示：

1 <= k <= s.length <= 100
s 中只含有小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """
        思路：区间dp
        1. 怎么计算一个字符串变为回文需要修改的次数
        2. 区间dp求分成k段需要修改的最少次数
        @param s:
        @param k:
        @return:
        """
        n = len(s)
        cost = [[0] * n for _ in range(n)]
        for span in range(2, n + 1):
            for l in range(n - span + 1):
                r = l + span - 1
                cost[l][r] = cost[l + 1][r - 1] + (0 if s[l] == s[r] else 1)

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if j == 1:
                    dp[i][j] = cost[0][i - 1]
                else:
                    for l in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[l][j - 1] + cost[l][i - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    s = "abc"
    k = 2
    print(Solution().palindromePartition(s, k))
