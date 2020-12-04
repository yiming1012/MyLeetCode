"""
1288. 删除被覆盖区间
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。

只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。

在完成所有删除操作后，请你返回列表中剩余区间的数目。

 

示例：

输入：intervals = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
 

提示：​​​​​​

1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
对于所有的 i != j：intervals[i] != intervals[j]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-covered-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def removeCoveredIntervals1(self, intervals: List[List[int]]) -> int:
        """
        思路：贪心
        1. 左端点顺序，右端点逆序
        2. 如果新的点右端点小于等于前面的点，删除，否则更新右端点
        @param intervals:
        @return:
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        n = len(intervals)
        for l, r in intervals:
            if stack:
                left, right = stack[-1]
                if right >= r:
                    n -= 1
                else:
                    if l >= right:
                        stack.append([l, r])
                    else:
                        stack[-1][1] = max(right, r)

            else:
                stack.append([l, r])
        return n

    def removeCoveredIntervals2(self, intervals: List[List[int]]) -> int:
        # Sort by start point.
        # If two intervals share the same start point
        # put the longer one to be the first.
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0

        prev_end = 0
        for _, end in intervals:
            # if current interval is not covered
            # by the previous one
            if end > prev_end:
                count += 1
                prev_end = end

        return count


if __name__ == '__main__':
    intervals = [[1, 4], [3, 6], [2, 8]]
    print(Solution().removeCoveredIntervals1(intervals))
    print(Solution().removeCoveredIntervals2(intervals))
