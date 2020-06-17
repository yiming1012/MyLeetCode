"""
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

返回一对观光景点能取得的最高分。

 

示例：

输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 

提示：

2 <= A.length <= 50000
1 <= A[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-sightseeing-pair
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        """
        思路：两数之和的最大值
        1、本题可以理解为（A[i]+i）和（A[j]-j）的最大值
        2、计算当前(preMax+A[i]+i)的最大值
        3、更新前面的最大值PreMax
        """
        res = float('-inf')
        preMax = A[0]
        for i in range(1, len(A)):
            res = max(preMax + A[i] - i, res)
            preMax = max(preMax, A[i] + i)
        return res


if __name__ == '__main__':
    A = [8, 1, 5, 2, 6]
    print(Solution().maxScoreSightseeingPair(A))
