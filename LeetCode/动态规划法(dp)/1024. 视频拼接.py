"""
1024. 视频拼接
你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。

视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。我们甚至可以对这些片段自由地再剪辑，例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。

我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。

 

示例 1：

输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
输出：3
解释：
我们选中 [0,2], [8,10], [1,9] 这三个片段。
然后，按下面的方案重制比赛片段：
将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
现在我们手上有 [0,2] + [2,8] + [8,10]，而这些涵盖了整场比赛 [0, 10]。
示例 2：

输入：clips = [[0,1],[1,2]], T = 5
输出：-1
解释：
我们无法只用 [0,1] 和 [1,2] 覆盖 [0,5] 的整个过程。
示例 3：

输入：clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
输出：3
解释：
我们选取片段 [0,4], [4,7] 和 [6,9] 。
示例 4：

输入：clips = [[0,4],[2,8]], T = 5
输出：2
解释：
注意，你可能录制超过比赛结束时间的视频。
 

提示：

1 <= clips.length <= 100
0 <= clips[i][0] <= clips[i][1] <= 100
0 <= T <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/video-stitching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def videoStitching1(self, clips: List[List[int]], T: int) -> int:
        """
        思路：动态规划法
        1. 获取每个位置对应的左边可以到达的最小位置，动态规划时从最小的位置转移
        @param clips:
        @param T:
        @return:
        """
        dp = [float('inf')] * (T + 1)
        dp[0] = 0
        pre = [float('inf')] * (100 + 1)
        for l, r in clips:
            for j in range(l, r + 1):
                pre[j] = min(pre[j], l)

        for i in range(1, T + 1):
            if pre[i] != float('inf'):
                dp[i] = min(dp[i], dp[pre[i]] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1

    def videoStitching2(self, clips: List[List[int]], T: int) -> int:
        """
        思路：贪心算法
        @param clips:
        @param T:
        @return:
        """
        if not T:
            return 0
        pre = [0] * (T + 1)
        for left, right in clips:
            if left <= T:
                pre[left] = max(pre[left], right)

        cur = nex = step = 0
        for i in range(T):
            nex = max(nex, pre[i])
            if nex >= T:
                return step + 1
            if nex == i:
                return -1
            if i == cur:
                step += 1
                cur = nex

        return -1


if __name__ == '__main__':
    clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    T = 10
    print(Solution().videoStitching1(clips, T))
    print(Solution().videoStitching2(clips, T))
