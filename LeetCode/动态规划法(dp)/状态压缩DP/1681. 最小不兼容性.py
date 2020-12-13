"""
1681. 最小不兼容性
给你一个整数数组 nums​​​ 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。

一个子集的 不兼容性 是该子集里面最大值和最小值的差。

请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 -1 。

子集的定义是数组中一些数字的集合，对数字顺序没有要求。

 

示例 1：

输入：nums = [1,2,1,4], k = 2
输出：4
解释：最优的分配是 [1,2] 和 [1,4] 。
不兼容性和为 (2-1) + (4-1) = 4 。
注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。
示例 2：

输入：nums = [6,3,8,1,3,1,2,2], k = 4
输出：6
解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。
示例 3：

输入：nums = [5,3,3,6,3,3], k = 3
输出：-1
解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。
 

提示：

1 <= k <= nums.length <= 16
nums.length 能被 k 整除。
1 <= nums[i] <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-incompatibility
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 如果n和k相等，每个子集的不兼容性为0
        if n == k:
            return 0
        # 每个子集的大小
        size = n // k
        # value记录每个合格子集的不兼容性
        value = collections.defaultdict()
        for sub in range(1 << n):
            # visited记录已遍历过的数，判断是否含有重复值
            visited = set()
            # 标记子集是否合法
            flag = True
            # 子集中最大最小值
            max_, min_ = float('-inf'), float('inf')
            # 判断sub中1的个数是否为size
            if bin(sub).count("1") == size:
                # 判断是否含有相同元素
                for i in range(n):
                    if sub >> i & 1:
                        if nums[i] in visited:
                            flag = False
                            break
                        max_ = max(max_, nums[i])
                        min_ = min(min_, nums[i])
                        visited.add(nums[i])
                # 计算不兼容性
                if flag:
                    value[sub] = max_ - min_

        # 状态压缩dp
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for i in range(1 << n):
            if bin(i).count("1") % size == 0:
                # 枚举子集
                sub = i
                while sub:
                    if sub in value:
                        # 更新状态
                        dp[i] = min(dp[i], dp[i ^ sub] + value[sub])
                    sub = (sub - 1) & i
        return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == '__main__':
    nums = [1, 2, 1, 4]
    k = 2
    print(Solution().minimumIncompatibility(nums, k))
