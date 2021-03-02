"""
1048. 最长字符串链
给出一个单词列表，其中每个单词都由小写英文字母组成。

如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac" 的前身。

词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。

从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。
 

示例：

输入：["a","b","ba","bca","bda","bdca"]
输出：4
解释：最长单词链之一为 "a","ba","bda","bdca"。
 

提示：

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] 仅由小写英文字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-string-chain
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        最长字符串链：可以联想到最长上升子序列
        @param words:
        @return:
        """
        dp = collections.defaultdict(lambda: 0)
        res = 0
        for w in sorted(words, key=len):
            for i in range(len(w)):
                dp[w] = max(dp[w], dp.get(w[:i] + w[i + 1:], 0) + 1)
            res = max(res, dp[w])
        return res


if __name__ == '__main__':
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(Solution().longestStrChain(words))
