"""
245. 最短单词距离 III
给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

word1 和 word2 是有可能相同的，并且它们将分别表示为列表中两个独立的单词。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"].

输入: word1 = “makes”, word2 = “coding”
输出: 1
输入: word1 = "makes", word2 = "makes"
输出: 3
注意:
你可以假设 word1 和 word2 都在列表里。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-word-distance-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
        思路：两点追逐问题
        @param wordsDict:
        @param word1:
        @param word2:
        @return:
        """
        self.dic = collections.defaultdict(list)
        self.index = collections.defaultdict(lambda: float('inf'))
        for i, w in enumerate(wordsDict):
            if self.dic[w]:
                self.index[w] = min(self.index[w], abs(self.dic[w][-1] - i))

            self.dic[w].append(i)

        if word1 == word2:
            return self.index[word1]

        res = float('inf')
        i, j = 0, 0
        while i < len(self.dic[word1]) and j < len(self.dic[word2]):
            res = min(res, abs(self.dic[word1][i] - self.dic[word2][j]))
            if self.dic[word1][i] < self.dic[word2][j]:
                i += 1
            else:
                j += 1
        return res


