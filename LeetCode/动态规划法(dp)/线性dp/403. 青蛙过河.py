"""
403. 青蛙过河
一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。

开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

 

示例 1：

输入：stones = [0,1,3,5,6,8,12,17]
输出：true
解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。
示例 2：

输入：stones = [0,1,2,3,4,8,9,11]
输出：false
解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
 

提示：

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/frog-jump
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import lru_cache
from typing import List


class Solution:
    def canCross1(self, stones: List[int]) -> bool:
        """
        思路：记忆化递归
        1. 递归出口：如果达到了最后位置，返回True
        2. 判断每个位置跳跃{k-1,k,k+1}后是否满足条件，满足则dfs到下一步
        3. 最后都没有找到则返回False
        @param stones:
        @return:
        """
        if stones[1] - stones[0] > 1: return False
        st = set(stones)

        @lru_cache(None)
        def dfs(k, pos):
            if pos == stones[-1]: return True
            for i in {-1, 0, 1}:
                if k + i > 0 and pos + k + i in st:
                    if dfs(k + i, pos + k + i):
                        return True

            return False

        ans = dfs(stones[1] - stones[0], stones[1])
        dfs.cache_clear()
        return ans

    def canCross2(self, stones: List[int]) -> bool:
        """
        思路：动态规划法
        1. 从后往前找，看看是否存在满足条件的
        @param stones:
        @return:
        """
        if stones[1] - stones[0] > 1: return False
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            if stones[i] - stones[i - 1] > i:
                return False

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                k = stones[i] - stones[j]
                if k > j + 1: break
                dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                if i == n - 1 and dp[i][k]:
                    return True

        return False


if __name__ == '__main__':
    stones = [0, 1, 3, 6, 10, 15, 21, 28]
    print(Solution().canCross1(stones))
    print(Solution().canCross2(stones))
