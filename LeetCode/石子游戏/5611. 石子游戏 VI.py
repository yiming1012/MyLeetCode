"""
5611. 石子游戏 VI
Alice 和 Bob 轮流玩一个游戏，Alice 先手。

一堆石子里总共有 n 个石子，轮到某个玩家时，他可以 移出 一个石子并得到这个石子的价值。Alice 和 Bob 对石子价值有 不一样的的评判标准 。

给你两个长度为 n 的整数数组 aliceValues 和 bobValues 。aliceValues[i] 和 bobValues[i] 分别表示 Alice 和 Bob 认为第 i 个石子的价值。

所有石子都被取完后，得分较高的人为胜者。如果两个玩家得分相同，那么为平局。两位玩家都会采用 最优策略 进行游戏。

请你推断游戏的结果，用如下的方式表示：

如果 Alice 赢，返回 1 。
如果 Bob 赢，返回 -1 。
如果游戏平局，返回 0 。
 

示例 1：

输入：aliceValues = [1,3], bobValues = [2,1]
输出：1
解释：
如果 Alice 拿石子 1 （下标从 0开始），那么 Alice 可以得到 3 分。
Bob 只能选择石子 0 ，得到 2 分。
Alice 获胜。
示例 2：

输入：aliceValues = [1,2], bobValues = [3,1]
输出：0
解释：
Alice 拿石子 0 ， Bob 拿石子 1 ，他们得分都为 1 分。
打平。
示例 3：

输入：aliceValues = [2,4,3], bobValues = [1,6,7]
输出：-1
解释：
不管 Alice 怎么操作，Bob 都可以得到比 Alice 更高的得分。
比方说，Alice 拿石子 1 ，Bob 拿石子 2 ， Alice 拿石子 0 ，Alice 会得到 6 分而 Bob 得分为 7 分。
Bob 会获胜。
 

提示：

n == aliceValues.length == bobValues.length
1 <= n <= 105
1 <= aliceValues[i], bobValues[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stone-game-vi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

"""
贪心做法：
证明：
假设只有两个石头,对于 a， b 的价值分别是 a1, a2, b1, b2

第一种方案是A取第一个，B取第二个，A与B的价值差是 c1 = a1 - b2
第二种方案是A取第二个，B取第一个，A与B的价值差是 c2 = a2 - b1
那么这两种方案对于A来说哪一种更优，就取决于两个方案的价值差的比较

记 c = c1 - c2 = （a1 - b2） - (a2 - b1) = (a1 + b1) - (a2 + b2)

如果c > 0 那么方案一更优，如果c == 0，那么两种方案价值一样，如果c < 0那么方案二更优

那么比较两个方案的优劣 == 比较 a1 + b1 与 a2 + b2 的优劣 ，
归纳一下就是比较每个下标 i 的 a[i] + b[i] 的优劣

所以贪心的策略：将两组石头的价值合并，每次取价值最大的那一组。

写法：先将两个数组的价值合并，并用下标去标记
对价值排序，A取偶数下标，B取奇数下标，最后比较A,B的价值总和

"""


class Solution:
    def stoneGameVI(self, a: List[int], b: List[int]) -> int:
        arr = list(zip(a, b))
        arr.sort(key=lambda x: x[0] + x[1], reverse=True)
        n = len(a)
        res_a, res_b = 0, 0
        for i in range(n):
            if i & 1 == 0:
                res_a += arr[i][0]
            else:
                res_b += arr[i][1]
        if res_a > res_b:
            return 1
        elif res_a < res_b:
            return -1
        else:
            return 0


if __name__ == '__main__':
    aliceValues = [1, 3]
    bobValues = [2, 1]
    print(Solution().stoneGameVI(aliceValues, bobValues))
