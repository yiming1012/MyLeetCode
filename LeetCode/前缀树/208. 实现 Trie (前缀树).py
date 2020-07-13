"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.dic
        for i in word:
            if i not in root:
                root[i] = {}
            root = root[i]
        root["#"] = "#"
        print(self.dic)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.dic
        for w in word:
            if w in root:
                root = root[w]
            else:
                return False
        if "#" in root:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.dic
        for w in prefix:
            if w in root:
                root = root[w]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
word = "abc"
prefix = "ab"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
print(param_2)
print(param_3)
