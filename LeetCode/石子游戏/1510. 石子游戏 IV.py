"""
Alice 和 Bob 两个人轮流玩一个游戏，Alice 先手。

一开始，有 n 个石子堆在一起。每个人轮流操作，正在操作的玩家可以从石子堆里拿走 任意 非零 平方数 个石子。

如果石子堆里没有石子了，则无法操作的玩家输掉游戏。

给你正整数 n ，且已知两个人都采取最优策略。如果 Alice 会赢得比赛，那么返回 True ，否则返回 False 。

 

示例 1：

输入：n = 1
输出：true
解释：Alice 拿走 1 个石子并赢得胜利，因为 Bob 无法进行任何操作。
示例 2：

输入：n = 2
输出：false
解释：Alice 只能拿走 1 个石子，然后 Bob 拿走最后一个石子并赢得胜利（2 -> 1 -> 0）。
示例 3：

输入：n = 4
输出：true
解释：n 已经是一个平方数，Alice 可以一次全拿掉 4 个石子并赢得胜利（4 -> 0）。
示例 4：

输入：n = 7
输出：false
解释：当 Bob 采取最优策略时，Alice 无法赢得比赛。
如果 Alice 一开始拿走 4 个石子， Bob 会拿走 1 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7 -> 3 -> 2 -> 1 -> 0）。
如果 Alice 一开始拿走 1 个石子， Bob 会拿走 4 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7 -> 6 -> 2 -> 1 -> 0）。
示例 5：

输入：n = 17
输出：false
解释：如果 Bob 采取最优策略，Alice 无法赢得胜利。
 

提示：

1 <= n <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stone-game-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        思路：只要取过石子之后，剩下的作为先手一定输，那么当前先手就直接赢
        """
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not dp[i - j ** 2]:
                    dp[i] = True
                    break
                j += 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().winnerSquareGame(7))
