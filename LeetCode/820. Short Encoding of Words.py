'''
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
 

Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/short-encoding-of-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from functools import reduce
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        '''
        执行用时 :148 ms, 在所有 Python3 提交中击败了56.52%的用户
        内存消耗 :14.3 MB, 在所有 Python3 提交中击败了8.33%的用户
        思路：将所有是其他单词后缀的词语删掉
        :param words:
        :return:
        '''
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)

    def minimumLengthEncoding2(self, words: List[str]) -> int:
        words = list(set(words))  # remove duplicates
        # Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
        print(nodes)
        for i in range(len(nodes)):
            print(i,nodes[i])

        # Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)



    def minimumLengthEncoding3(self, words: List[str]) -> int:
        words = sorted(w[:: -1] for w in words)
        print(words)
        print([len(words[i]) + 1 for i, w in enumerate(words[1:]) if w.startswith(words[i])])
        for i, w in enumerate(words[1:]):
            print(i, w, words[i])
        print([(map(len, words))])
        return sum(map(len, words)) + len(words) - sum(
            len(words[i]) + 1 for i, w in enumerate(words[1:]) if w.startswith(words[i]))


if __name__ == '__main__':
    words = ["time", "me", "bell", "el", "be"]
    s = Solution()
    print(s.minimumLengthEncoding2(words))
