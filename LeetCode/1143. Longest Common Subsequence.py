'''
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        执行用时 :460 ms, 在所有 Python3 提交中击败了70.37%的用户
        内存消耗 :22.1 MB, 在所有 Python3 提交中击败了10.71%的用户
        时间复杂度：O(n*n)
        空间复杂度：O(n*n)
        :param text1:
        :param text2:
        :return:
        '''

        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 比上面效率高，由20%->70%

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        '''
        执行用时 :380 ms, 在所有 Python3 提交中击败了96.30%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了89.29%的用户
        思路：将空间复杂度降为O(1)
        :param text1:
        :param text2:
        :return:
        '''
        m = len(text1)
        n = len(text2)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            left = 0
            for j in range(1, n + 1):
                rightTop = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = left + 1
                else:
                    dp[j] = max(dp[j - 1], rightTop)
                left = rightTop

        return dp[-1]

    def backTracking(self, i, j, arr):
        print(i, j)
        if i == 0 or j == 0:
            total.append(tuple(arr[::-1]))
            return
        # if len(arr) == 3:
        #     total.append(tuple(arr[::-1]))
        #     return

        if text1[i - 1] == text2[j - 1]:
            arr.append(text1[i - 1])
            self.backTracking(i - 1, j - 1, arr)
            arr.pop()

        elif dp[i - 1][j] > dp[i][j - 1]:
            self.backTracking(i - 1, j, arr)
        elif dp[i][j - 1] > dp[i - 1][j]:
            self.backTracking(i, j - 1, arr)
        else:
            self.backTracking(i - 1, j, arr)
            self.backTracking(i, j - 1, arr)

    def backTracking2(self, i, j, arr):
        print(i, j)
        if i == 0 or j == 0:
            total.append(tuple(arr[::-1]))
            return

        if dp[i - 1][j] == dp[i][j - 1] == dp[i - 1][j - 1] and dp[i][j] == dp[i - 1][j - 1] + 1:
            arr.append(text1[i - 1])
            self.backTracking(i - 1, j - 1, arr)
            arr.pop()

        elif dp[i - 1][j] == dp[i][j]:
            self.backTracking(i - 1, j, arr)

        elif dp[i][j - 1] > dp[i][j]:
            self.backTracking(i, j - 1, arr)

    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequence2(text1, text2)
        dps = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            ii = i - 1
            for j in range(1, len(text2) + 1):
                jj = j - 1
                if text1[ii] == text2[jj]:
                    dps[i][j] = dps[i - 1][j - 1] + 1
                else:
                    dps[i][j] = max(dps[i - 1][j], dps[i][j - 1])

        # return dps[-1][-1]
        def backtrack(one_route, all_routes, i, j):
            if i == 0 or j == 0:
                all_routes.add(tuple(one_route[::-1]))
                return

            ii = i - 1
            jj = j - 1
            if text1[ii] == text2[jj]:
                one_route.append(text1[ii])
                backtrack(one_route, all_routes, i - 1, j - 1)
                one_route.pop()
            elif dps[i - 1][j] > dps[i][j - 1]:
                backtrack(one_route, all_routes, i - 1, j)
            elif dps[i - 1][j] < dps[i][j - 1]:
                backtrack(one_route, all_routes, i, j - 1)
            else:
                backtrack(one_route, all_routes, i - 1, j)
                backtrack(one_route, all_routes, i, j - 1)

        one_route = []
        all_routes = set()
        backtrack(one_route, all_routes, i=len(text1), j=len(text2))
        return len(list(all_routes)[-1])
        # return dps[-1][-1]

    def longestCommonSubsequence4(self, text1: str, text2: str) -> int:
        dps = [0] * (1 + len(text2))
        for i in range(1, len(text1) + 1):
            lu = dps[0]
            for j in range(1, len(text2) + 1):
                ii = i - 1
                jj = j - 1
                if text1[ii] == text2[jj]:
                    lu, dps[j] = dps[j], lu + 1
                else:
                    lu, dps[j] = dps[j], max(dps[j], dps[j - 1])
        return dps[-1]


if __name__ == '__main__':
    text1 = "abc"
    text2 = "abc"
    s = Solution()
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    print(s.longestCommonSubsequence(text1, text2))
    # get longest common subsequence
    total = []
    s.backTracking(m, n, [])
    print(total)
