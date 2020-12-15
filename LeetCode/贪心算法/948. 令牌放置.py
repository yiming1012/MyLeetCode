"""
948. 令牌放置
你的初始 能量 为 P，初始 分数 为 0，只有一包令牌 tokens 。其中 tokens[i] 是第 i 个令牌的值（下标从 0 开始）。

令牌可能的两种使用方法如下：

如果你至少有 token[i] 点 能量 ，可以将令牌 i 置为正面朝上，失去 token[i] 点 能量 ，并得到 1 分 。
如果我们至少有 1 分 ，可以将令牌 i 置为反面朝上，获得 token[i] 点 能量 ，并失去 1 分 。
每个令牌 最多 只能使用一次，使用 顺序不限 ，不需 使用所有令牌。

在使用任意数量的令牌后，返回我们可以得到的最大 分数 。

 

示例 1：

输入：tokens = [100], P = 50
输出：0
解释：无法使用唯一的令牌，因为能量和分数都太少了。
示例 2：

输入：tokens = [100,200], P = 150
输出：1
解释：令牌 0 正面朝上，能量变为 50，分数变为 1 。不必使用令牌 1 ，因为你无法使用它来提高分数。
示例 3：

输入：tokens = [100,200,300,400], P = 200
输出：2
解释：按下面顺序使用令牌可以得到 2 分：
1. 令牌 0 正面朝上，能量变为 100 ，分数变为 1
2. 令牌 3 正面朝下，能量变为 500 ，分数变为 0
3. 令牌 1 正面朝上，能量变为 300 ，分数变为 1
4. 令牌 2 正面朝上，能量变为 0 ，分数变为 2
 

提示：

0 <= tokens.length <= 1000
0 <= tokens[i], P < 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bag-of-tokens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        """
        思路：贪心算法
        1. 排序tokens
        2. 从左到右，如果P大于tokens[i]，则获得分数
        3. 如果有分数，但能量不够，则用分数换取最大的能量
        @param tokens:
        @param P:
        @return:
        """
        tokens.sort()
        score = 0

        queue = collections.deque()
        for t in tokens:
            queue.append(t)

        while queue:
            if P >= queue[0]:
                P -= queue.popleft()
                score += 1
            elif score > 0:
                if len(queue) > 1:
                    P += queue.pop()
                    score -= 1
                else:
                    break
            else:
                return 0

        return score