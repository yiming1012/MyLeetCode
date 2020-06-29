'''
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be
             removed by your friend.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nim-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def canWinNim(self, n: int) -> bool:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了13.80%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.17%的用户
        思路：自己选择时候，余数必须为4的整数倍，自己才能赢
        :param n:
        :return:
        '''
        return n % 4 > 0

    def canWinNim(self, n: int) -> bool:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了29.48%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.17%的用户
        思路:// %效率较低，+ & * 效率高
        :param n:
        :return:
        '''
        return n & 3
