"""
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        思路：位运算
        1. 将a~z 26个英文字母对应从低到高的26位二进制，示例：a对应为0001，b对应0010
        2. 如果两个字符串对应的二进制进行与运算&，结果为0，说明两个单词没有相同的字符，计算两者长度乘积即可
        @param words:
        @return:
        """
        n = len(words)
        dic = {}
        for word in words:
            bitmask = 0
            for c in word:
                bitmask |= 1 << (ord(c) - 97)
            dic[word] = bitmask

        res = 0
        for i in range(n - 1):
            w1 = words[i]
            for j in range(i + 1, n):
                w2 = words[j]
                if dic[w1] & dic[w2] == 0:
                    res = max(res, len(w1) * len(w2))
        return res


if __name__ == '__main__':
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    print(Solution().maxProduct(words))
