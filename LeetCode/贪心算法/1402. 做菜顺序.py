"""
一个厨师收集了他 n 道菜的满意程度 satisfaction ，这个厨师做出每道菜的时间都是 1 单位时间。

一道菜的 「喜爱时间」系数定义为烹饪这道菜以及之前每道菜所花费的时间乘以这道菜的满意程度，也就是 time[i]*satisfaction[i] 。

请你返回做完所有菜 「喜爱时间」总和的最大值为多少。

你可以按 任意 顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。

 

示例 1：

输入：satisfaction = [-1,-8,0,5,-9]
输出：14
解释：去掉第二道和最后一道菜，最大的喜爱时间系数和为 (-1*1 + 0*2 + 5*3 = 14) 。每道菜都需要花费 1 单位时间完成。
示例 2：

输入：satisfaction = [4,3,2]
输出：20
解释：按照原来顺序相反的时间做菜 (2*1 + 3*2 + 4*3 = 20)
示例 3：

输入：satisfaction = [-1,-4,-5]
输出：0
解释：大家都不喜欢这些菜，所以不做任何菜可以获得最大的喜爱时间系数。
示例 4：

输入：satisfaction = [-2,5,-1,0,3,-3]
输出：35
 

提示：

n == satisfaction.length
1 <= n <= 500
-10^3 <= satisfaction[i] <= 10^3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reducing-dishes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        思路：累乘
        1. 1*a +2*b + 3*c 可以考虑从后面往前加pre+num，res每次加上pre,后面的数会被加n次
        @param satisfaction:
        @return:
        """
        arr = sorted(satisfaction, reverse=True)
        res, pre = 0, 0
        for num in arr:
            if num + pre > 0:
                pre += num
                res += pre
            else:
                break
        return res


if __name__ == '__main__':
    satisfaction = [-1, -8, 0, 5, -9]
    print(Solution().maxSatisfaction(satisfaction))
