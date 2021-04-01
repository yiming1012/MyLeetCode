"""
1032. 字符流
按下述要求实现 StreamChecker 类：

StreamChecker(words)：构造函数，用给定的字词初始化数据结构。
query(letter)：如果存在某些 k >= 1，可以用查询的最后 k个字符（按从旧到新顺序，包括刚刚查询的字母）拼写出给定字词表中的某一字词时，返回 true。否则，返回 false。
 

示例：

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // 初始化字典
streamChecker.query('a');          // 返回 false
streamChecker.query('b');          // 返回 false
streamChecker.query('c');          // 返回 false
streamChecker.query('d');          // 返回 true，因为 'cd' 在字词表中
streamChecker.query('e');          // 返回 false
streamChecker.query('f');          // 返回 true，因为 'f' 在字词表中
streamChecker.query('g');          // 返回 false
streamChecker.query('h');          // 返回 false
streamChecker.query('i');          // 返回 false
streamChecker.query('j');          // 返回 false
streamChecker.query('k');          // 返回 false
streamChecker.query('l');          // 返回 true，因为 'kl' 在字词表中。
 

提示：

1 <= words.length <= 2000
1 <= words[i].length <= 2000
字词只包含小写英文字母。
待查项只包含小写英文字母。
待查项最多 40000 个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stream-of-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stack = collections.deque()
        self.trie = {}
        for word in words:
            self.insert(word[::-1])

    def insert(self, word):
        root = self.trie
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root['#'] = '#'

    def search(self, word):
        root = self.trie
        for c in word:
            if c in root:
                root = root[c]
                if '#' in root:
                    return True
            else:
                return False
        return False

    def query(self, letter: str) -> bool:
        self.stack.appendleft(letter)
        return self.search(self.stack)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
