"""
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数

 

示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
提示：

0 <= len(sentence) <= 1000
dictionary中总字符数不超过 150000。
你可以认为dictionary和sentence中只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/re-space-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def respace1(self, dictionary: List[str], sentence: str) -> int:
        dp = [0] * (len(sentence) + 1)
        for i in range(len(sentence)):
            dp[i + 1] = dp[i] + 1
            for s in dictionary:
                if i + 1 - len(s) >= 0 and sentence[i + 1 - len(s):i + 1] == s:
                    dp[i + 1] = min(dp[i + 1], dp[i + 1 - len(s)])
        return dp[-1]

    def respace2(self, dictionary: List[str], sentence: str) -> int:
        """
           动态规划
           状态定义：f[i]，0 <= i <= len(sentence)
               集合：前 i 个字符所有可能的划分方式
               属性：Min(未识别的字符数)
           状态转移：
               集合划分：
                   第 i 个字符无法与前面任何一个子串组成单词：f[i - 1] + 1
                   第 i 个字符可以与前面某个子串组成单词：f[j]
                   if sentence[j:i] in dictionary，0 <= j <= i - 1
               初始化：f[0] = 0，当 sentence 为空字符串时，未识别字符数为 0
               答案：f[-1]
           """
        d = {}.fromkeys(dictionary)
        n = len(sentence)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + 1
            for j in range(i):
                if sentence[j:i] in d:
                    f[i] = min(f[i], f[j])
        return f[-1]

    def respace3(self, dictionary: List[str], sentence: str) -> int:
        dic = collections.defaultdict()
        for word in dictionary:
            root = dic
            for c in word:
                if c not in root:
                    root[c] = {}
                root = root[c]

        def dfs(child, s):
            if not child:
                res.append(s)

            for k, v in child.items():
                print(k, v)
                dfs(v, s + k)
            print(dic)

        res = []
        dfs(dic, "")
        print(res)

        dp = [0] * (len(sentence) + 1)
        for i in range(len(sentence)):
            dp[i + 1] = dp[i] + 1
            for s in dictionary:
                if i + 1 - len(s) >= 0 and sentence[i + 1 - len(s):i + 1] == s:
                    dp[i + 1] = min(dp[i + 1], dp[i + 1 - len(s)])
        return dp[-1]


if __name__ == '__main__':
    dictionary = ["looked", "just", "like", "her", "brother", "he", "look", "the", "her"]
    sentence = "jesslookedjustliketimherbrother"
    print(Solution().respace1(dictionary, sentence))
    print(Solution().respace2(dictionary, sentence))
    print(Solution().respace3(dictionary, sentence))
