"""
290. 单词规律
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def wordPattern1(self, pattern: str, s: str) -> bool:
        """
        巧用zip判断一行中是否有重复值
        @param pattern:
        @param s:
        @return:
        """
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        for l in zip(*set(zip(list(pattern), words))):
            if len(l) != len(set(l)):
                return False
        return True

    def wordPattern2(self, pattern: str, s: str) -> bool:
        """
        两个dict分别记录pattern和s对应的值
        @param pattern:
        @param s:
        @return:
        """
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False

        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word

        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "cat dog dog cat"
    print(Solution().wordPattern1(pattern, s))
    print(Solution().wordPattern2(pattern, s))
