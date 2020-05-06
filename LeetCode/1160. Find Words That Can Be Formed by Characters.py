'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''
        执行用时 :280 ms, 在所有 Python3 提交中击败了31.76%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.11%的用户
        :param words:
        :param chars:
        :return:
        '''
        count = 0
        for word in words:
            a = list(chars)
            # print(a)
            flag = 1
            for s in word:
                if s not in a:
                    flag = 0
                    break
                a.remove(s)
            if flag == 1:
                count += len(word)

        return count

    def countCharacters2(self, words: List[str], chars: str) -> int:
        '''
        执行用时 :104 ms, 在所有 Python3 提交中击败了91.45%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.11%的用户
        :param words:
        :param chars:
        :return:
        '''
        count = 0
        for word in words:
            for s in word:
                if word.count(s) > chars.count(s):
                    break

            else:
                count += len(word)

        return count

    def countCharacters3(self, words: List[str], chars: str) -> int:
        '''
        执行用时 :216 ms, 在所有 Python3 提交中击败了48.70%的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.11%的用户
        :param words:
        :param chars:
        :return:
        '''
        a = collections.Counter(chars)
        # print(a)
        count = 0
        for word in words:
            b = collections.Counter(word)
            for s in b:
                # print(s,b[s],a[s])
                if b[s] > a[s]:
                    break

            else:
                count += len(word)

        return count

if __name__ == '__main__':
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    s = Solution()
    print(s.countCharacters(words, chars))
