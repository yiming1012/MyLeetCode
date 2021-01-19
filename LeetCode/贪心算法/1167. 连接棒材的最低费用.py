"""
1167. 连接棒材的最低费用
为了装修新房，你需要加工一些长度为正整数的棒材 。棒材以数组 sticks 的形式给出，其中 sticks[i] 是第 i 根棒材的长度。

如果要将长度分别为 x 和 y 的两根棒材连接在一起，你需要支付 x + y 的费用。 由于施工需要，你必须将所有棒材连接成一根。

返回你把所有棒材 sticks 连成一根所需要的最低费用。注意你可以任意选择棒材连接的顺序。

 

示例 1：

输入：sticks = [2,4,3]
输出：14
解释：从 sticks = [2,4,3] 开始。
1. 连接 2 和 3 ，费用为 2 + 3 = 5 。现在 sticks = [5,4]
2. 连接 5 和 4 ，费用为 5 + 4 = 9 。现在 sticks = [9]
所有棒材已经连成一根，总费用 5 + 9 = 14
示例 2：

输入：sticks = [1,8,3,5]
输出：30
解释：从 sticks = [1,8,3,5] 开始。
1. 连接 1 和 3 ，费用为 1 + 3 = 4 。现在 sticks = [4,8,5]
2. 连接 4 和 5 ，费用为 4 + 5 = 9 。现在 sticks = [9,8]
3. 连接 9 和 8 ，费用为 9 + 8 = 17 。现在 sticks = [17]
所有棒材已经连成一根，总费用 4 + 9 + 17 = 30
示例 3：

输入：sticks = [5]
输出：0
解释：只有一根棒材，不必再连接。总费用 0
 

提示：

1 <= sticks.length <= 104
1 <= sticks[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-cost-to-connect-sticks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        思路：贪心算法+哈夫曼树
        @param sticks:
        @return:
        """
        n = len(sticks)
        if n == 1:
            return 0
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            heapq.heappush(sticks, a + b)
            res += a + b
        return res


if __name__ == '__main__':
    sticks = [2, 4, 3]
    print(Solution().connectSticks(sticks))
