"""
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        思路：单向BFS
        @param beginWord:
        @param endWord:
        @param wordList:
        @return:
        """
        st = set(wordList)
        if endWord not in st:
            return 0
        m = len(beginWord)
        visited = set()
        queue = collections.deque()
        visited.add(beginWord)
        queue.append((beginWord, 1))

        while queue:
            cur, step = queue.popleft()
            if cur == endWord:
                return step

            new_list = list(cur)
            for i in range(m):
                c_i = new_list[i]
                for j in range(26):
                    new_list[i] = chr(97 + j)
                    new_word = "".join(new_list)
                    if new_word not in visited and new_word in st:
                        queue.append((new_word, step + 1))
                        visited.add(new_word)
                    new_list[i] = c_i
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        思路：双向BFS
        @param beginWord:
        @param endWord:
        @param wordList:
        @return:
        """
        st = set(wordList)
        if endWord not in st:
            return 0
        m = len(beginWord)
        lvisited = set()
        rvisited = set()
        lqueue = collections.deque()
        rqueue = collections.deque()

        lqueue.append(beginWord)
        rqueue.append(endWord)

        lvisited.add(beginWord)
        rvisited.add(endWord)
        step = 0

        while lqueue and rqueue:
            if len(lqueue) > len(rqueue):
                lqueue, rqueue = rqueue, lqueue
                lvisited, rvisited = rvisited, lvisited

            step += 1
            for k in range(len(lqueue)):
                cur = lqueue.popleft()
                if cur in rvisited:
                    return step

                for i in range(m):
                    for j in range(26):
                        tmp = cur[:i] + str(chr(97 + j)) + cur[i + 1:]
                        if tmp not in lvisited and tmp in st:
                            lqueue.append(tmp)
                            lvisited.add(tmp)

        return 0


if __name__ == '__main__':
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))
