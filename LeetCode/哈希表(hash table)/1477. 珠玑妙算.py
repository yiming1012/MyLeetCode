'''
The Game of Master Mind is played as follows:

The computer has four slots, and each slot will contain a ball that is red (R). yellow (Y). green (G) or blue (B). For example, the computer might have RGGB (Slot #1 is red, Slots #2 and #3 are green, Slot #4 is blue).

You, the user, are trying to guess the solution. You might, for example, guess YRGB.

When you guess the correct color for the correct slot, you get a "hit:' If you guess a color that exists but is in the wrong slot, you get a "pseudo-hit:' Note that a slot that is a hit can never count as a pseudo-hit.

For example, if the actual solution is RGBY and you guess GGRR, you have one hit and one pseudo-hit. Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits.

Given a sequence of colors solution, and a guess, write a method that return the number of hits and pseudo-hit answer, where answer[0] is the number of hits and answer[1] is the number of pseudo-hit.

Example:

Input:  solution="RGBY",guess="GGRR"
Output:  [1,1]
Explanation:  hit once, pseudo-hit once.
Note:

len(solution) = len(guess) = 4
There are only "R","G","B","Y" in solution and guess.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/master-mind-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from typing import List


class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了71.07%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：
        1、求交集
        2、拉链操作zip
        :param solution:
        :param guess:
        :return:
        '''
        dic1 = collections.Counter(solution)
        dic2 = collections.Counter(guess)
        b = sum((dic1 & dic2).values())
        a = sum([int(i == j) for i, j in zip(solution, guess)])
        return [a, b - a]


if __name__ == '__main__':
    solution = "RGBY"
    guess = "GGRR"
    s = Solution()
    print(s.masterMind(solution, guess))
