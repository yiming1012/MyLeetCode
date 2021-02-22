class Solution:
    def longestPalindrome1(self, s: str) -> str:
        """
        执行用时 :936 ms, 在所有 Python3 提交中击败了81.31%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了9.26%的用户
        思路：找到一个单词i从两边扩散，如果遇到重复的就向右边扩散j+1,最后判断i-1和j+1位置的元素是否相等
        还可以优化：只保留每次的最大长度，而不用生成新的字符串
        """
        res = ""
        n = len(s)
        k = 0
        while k < n:
            i = j = k
            while j + 1 < n and s[j + 1] == s[j]:
                j += 1
            while i - 1 >= 0 and j + 1 < n and s[i - 1] == s[j + 1]:
                i -= 1
                j += 1
            if j + 1 - i > len(res):
                res = s[i:j + 1]
            k += 1
        return res

    def longestPalindrome2(self, s: str) -> str:
        """
        思路：动态规划法 dp[i][j]表示i到j的字符串为回文
        1. 如果i和j的位置字符相同，则判断s[i+1:j]是不是回文
        2. 边界问题：如果j-1-(i)+1<1
        3. 状态转移方程：dp[i][j]= s[i]==s[j] and dp[i+1][j-1]
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for j in range(n):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = 0
                else:
                    if j - i < 3:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
        length = 0
        start = 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] == 1 and j - i + 1 > length:
                    length = j - i + 1
                    start = i
        return s[start:start + length]

    def longestPalindrome3(self, s: str) -> str:
        """
        Manacher（马拉车）算法
        @param s:
        @return:
        """
        def getLength(i, j):
            while i - 1 >= 0 and j + 1 < n and S[i - 1] == S[j + 1]:
                i -= 1
                j += 1
            return (j - i + 2) // 2

        S = "#" + "#".join(list(s)) + "#"
        start, end = -1, -1
        center, right = 0, 0
        n = len(S)
        dp = [0] * n
        for i in range(n):
            if right > i:
                j = 2 * center - i
                arm = min(dp[j], right - i + 1)
                max_arm = getLength(i - arm + 1, i + arm - 1)
            else:
                max_arm = getLength(i, i)

            dp[i] = max_arm
            if i + max_arm - 1 > right:
                right = i + max_arm - 1
                center = i

                if 2 * max_arm - 1 > end - start + 1:
                    start, end = i - max_arm + 1, i + max_arm - 1
        return S[start + 1:end:2]


'''
1、最先想到的是中心查找，分两种情况：abba和aba。
2、官方答案很巧妙的将重复的字符当成同一个字符处理,i移动到最后面的一个相同字符
不仅方便可以确定起始和终止位置，还可以减少遍历，直接从最后一个相同字符下一个开始遍历
'''

if __name__ == '__main__':
    s = "aabbaa"
    s2 = "aacabdkacaa"
    print(Solution().longestPalindrome1(s))
    print(Solution().longestPalindrome2(s2))
    print(Solution().longestPalindrome3(s2))
