'''

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
import collections
from typing import List


class Solution:
    def letterCombinations1(self, digits: str) -> List[str]:
        """
        思路：回溯法模板
        @param digits:
        @return:
        """
        if not digits:
            return []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        n = len(digits)

        def dfs(cur, arr):
            if len(arr) == n:
                res.append("".join(arr))
                return

            s = dic[digits[cur]]
            for c in s:
                dfs(cur + 1, arr + [c])

        res = []
        dfs(0, [])
        return res

    def letterCombinations2(self, digits: str) -> List[str]:
        """
        思路：
        @param digits:
        @return:
        """
        if not digits:
            return []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = [""]
        for i in range(len(digits)):
            res = [x + y for x in res for y in dic[digits[i]]]
        return res

    def letterCombinations3(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = [""]
        n = len(digits)
        queue = collections.deque()
        queue.append("")

        i = 0
        while i < n:
            for j in range(len(queue)):
                num = queue.popleft()
                for c in dic[digits[i]]:
                    queue.append(num + c)
            i += 1
        return list(queue)


if __name__ == '__main__':
    digits = "23"
    print(Solution().letterCombinations1(digits))
    print(Solution().letterCombinations2(digits))
    print(Solution().letterCombinations3(digits))
