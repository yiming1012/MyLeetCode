"""
244. 最短单词距离 II
请设计一个类，使该类的构造函数能够接收一个单词列表。然后再实现一个方法，该方法能够分别接收两个单词 word1 和 word2，并返回列表中这两个单词之间的最短距离。您的方法将被以不同的参数调用 多次。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = “coding”, word2 = “practice”
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1
注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-word-distance-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from bisect import bisect
from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dic = collections.defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.dic[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        arr1 = self.dic[word1]
        arr2 = self.dic[word2]
        res = float('inf')
        for i in arr1:
            index = bisect.bisect_left(arr2, i)
            if index < len(arr2):
                res = min(res, abs(i - arr2[index]))
            if index > 0:
                res = min(res, abs(i - arr2[index - 1]))
            if index < len(arr2) - 1:
                res = min(res, abs(i - arr2[index + 1]))
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)