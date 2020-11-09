"""
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换后得到的单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        st = set(wordList)
        if endWord not in st:
            return []

        m = len(beginWord)

        visited = set()
        visited.add(beginWord)

        queue = collections.deque()
        queue.append(beginWord)

        graph = collections.defaultdict(set)
        flag = False
        step = 0
        while queue:
            step += 1
            next_visited = set()
            for k in range(len(queue)):
                cur = queue.popleft()

                for i in range(m):
                    for j in range(26):
                        tmp = cur[:i] + chr(97 + j) + cur[i + 1:]
                        if tmp != cur and tmp in st and tmp not in visited:
                            if tmp == endWord:
                                flag = True
                            # 防止下一层的元素被标记为访问过后，本层的元素不能到达
                            if tmp not in next_visited:
                                queue.append(tmp)
                                next_visited.add(tmp)
                            graph[cur].add(tmp)

            if flag:
                step += 1
                break
            # 合并本层和下层的visited
            visited |= next_visited

        if step == 0:
            return []

        ans = []

        def dfs(cur, arr):
            if cur == endWord:
                ans.append(arr.copy())
                return
            for node in graph[cur]:
                dfs(node, arr + [node])

        dfs(beginWord, [beginWord])
        return ans


if __name__ == '__main__':
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().findLadders(beginWord, endWord, wordList))
