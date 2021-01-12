"""
5639. 完成所有工作的最短时间
给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。

请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。

返回分配方案中尽可能 最小 的 最大工作时间 。

 

示例 1：

输入：jobs = [3,2,3], k = 3
输出：3
解释：给每位工人分配一项工作，最大工作时间是 3 。
示例 2：

输入：jobs = [1,2,4,7,8], k = 2
输出：11
解释：按下述方式分配工作：
1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
2 号工人：4、7（工作时间 = 4 + 7 = 11）
最大工作时间是 11 。
 

提示：

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)

        # check
        def check(target):
            dp = [float('inf')] * (1 << n)
            dp[0] = 0
            for mask in range(1 << n):
                sub = mask
                while sub:
                    if score[sub] <= target:
                        dp[mask] = min(dp[mask], dp[mask ^ sub] + 1)
                    sub = (sub - 1) & mask
            return dp[-1] <= k

        # 计算每个数对应的值
        score = [0] * (1 << n)
        for i in range(1 << n):
            for j in range(n):
                if i >> j & 1:
                    score[i] += jobs[j]
        print(score)
        l, r = max(jobs), sum(jobs)
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    jobs = [1, 2, 4]
    k = 3
    print(Solution().minimumTimeRequired(jobs, k))
