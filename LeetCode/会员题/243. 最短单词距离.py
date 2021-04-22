"""
243. 最短单词距离
给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = “coding”, word2 = “practice”
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1
注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-word-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
        思路：双指针
        @param wordsDict:
        @param word1:
        @param word2:
        @return:
        """
        i1 = i2 = -1
        res = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            if word == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                res = min(res, abs(i1 - i2))
        return res


    


if __name__ == '__main__':
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    print(Solution().shortestDistance(wordsDict, word1, word2))
