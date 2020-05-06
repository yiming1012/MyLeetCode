'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].
 

Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
import functools
import math
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了94.56%的用户
        内存消耗 :14 MB, 在所有 Python3 提交中击败了5.38%的用户
        :param deck:
        :return:
        '''
        if len(deck) <= 1:
            return False
        dic = dict(collections.Counter(deck))

        value = list(dic.values())

        if len(value) == 1:
            return True

        def gcd(a, b):
            while a:
                a, b = b % a, a
            return b

        # 求最大公约数
        for i in range(len(value) - 1):
            for j in range(i + 1, len(value)):
                if gcd(value[i], value[j]) == 1:
                    return False
        return True

    def hasGroupsSizeX2(self, deck: List[int]) -> bool:
        return functools.reduce(math.gcd, collections.Counter(deck).values()) >= 2


if __name__ == '__main__':
    # deck = [1,1,1][0,0,0,0,0,1,1,2,3,4]
    deck = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]
    s = Solution()
    print(s.hasGroupsSizeX2(deck))
