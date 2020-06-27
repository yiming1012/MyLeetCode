"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import lru_cache
from typing import List


class Solution:
    """
    题意：判断给定的s能否由wordDict中的word连起来，word可以使用多次
    """
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        """
        思路：动态规划法
        1. 判断s中每个位置前面是否有
        """
        # 数组转set，让查询的时候复杂度由O(N)变为O(1)
        dic = {*wordDict}
        # dic =set(wordDict)
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in wordDict:
                # 判断当前的word的
                if s[i - len(j):i] in dic and dp[i - len(j)] == 1:
                    dp[i] = 1
                    break
        return True if dp[-1] == 1 else False

    flag = 0

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        """
        思路：dfs
        1. 用字符串s去wordDict中匹配，匹配到就从s剩下的字符串中匹配wordDict，直到正好匹配完s
        2.
        """
        @lru_cache()
        def dfs(l):
            if l == len(s):
                self.flag = 1
                return

            for word in wordDict:
                if len(s[l:]) >= len(word) and s[l:].startswith(word):
                    dfs(l + len(word))

        dfs(0)
        return True if self.flag == 1 else False