"""
LCP 12. 小张刷题计划
为了提高自己的代码能力，小张制定了 LeetCode 刷题计划，他选中了 LeetCode 题库中的 n 道题，编号从 0 到 n-1，并计划在 m 天内按照题目编号顺序刷完所有的题目（注意，小张不能用多天完成同一题）。

在小张刷题计划中，小张需要用 time[i] 的时间完成编号 i 的题目。此外，小张还可以使用场外求助功能，通过询问他的好朋友小杨题目的解法，可以省去该题的做题时间。为了防止“小张刷题计划”变成“小杨刷题计划”，小张每天最多使用一次求助。

我们定义 m 天中做题时间最多的一天耗时为 T（小杨完成的题目不计入做题总时间）。请你帮小张求出最小的 T是多少。

示例 1：

输入：time = [1,2,3,3], m = 2

输出：3

解释：第一天小张完成前三题，其中第三题找小杨帮忙；第二天完成第四题，并且找小杨帮忙。这样做题时间最多的一天花费了 3 的时间，并且这个值是最小的。

示例 2：

输入：time = [999,999,999], m = 4

输出：0

解释：在前三天中，小张每天求助小杨一次，这样他可以在三天内完成所有的题目并不花任何时间。

 

限制：

1 <= time.length <= 10^5
1 <= time[i] <= 10000
1 <= m <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xiao-zhang-shua-ti-ji-hua
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        """
        思路：前缀和-最大值 如果大于x的话 天数+1
        @param time:
        @param m:
        @return:
        """

        def check(x):
            pre, cnt = 0, 1
            maxv = float('-inf')
            for t in time:
                pre += t
                maxv = max(maxv, t)
                if pre - maxv > x:
                    cnt += 1
                    pre = t
                    maxv = t
            return cnt <= m

        l, r = 0, sum(time)
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    time = [1, 2, 3, 3]
    m = 2
    print(Solution().minTime(time, m))
