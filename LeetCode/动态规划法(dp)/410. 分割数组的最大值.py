"""
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-largest-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        思路与算法

「将数组分割为 mm 段，求……」是动态规划题目常见的问法。

本题中，我们可以令 f[i][j]f[i][j] 表示将数组的前 ii 个数分割为 jj 段所能得到的最大连续子数组和的最小值。在进行状态转移时，我们可以考虑第 jj 段的具体范围，即我们可以枚举 kk，其中前 kk 个数被分割为 j-1j−1 段，而第 k+1k+1 到第 ii 个数为第 jj 段。此时，这 jj 段子数组中和的最大值，就等于 f[k][j-1]f[k][j−1] 与 \textit{sub}(k+1, i)sub(k+1,i) 中的较大值，其中 \textit{sub}(i,j)sub(i,j) 表示数组 \textit{nums}nums 中下标落在区间 [i,j][i,j] 内的数的和。

由于我们要使得子数组中和的最大值最小，因此可以列出如下的状态转移方程：

f[i][j] = \min_{k=0}^{i-1} \Big\{ \max(f[k][j-1], \textit{sub}(k+1,i)) \Big\}
f[i][j]=
k=0
min
i−1
​
 {max(f[k][j−1],sub(k+1,i))}

对于状态 f[i][j]f[i][j]，由于我们不能分出空的子数组，因此合法的状态必须有 i \geq ji≥j。对于不合法（i < ji<j）的状态，由于我们的目标是求出最小值，因此可以将这些状态全部初始化为一个很大的数。在上述的状态转移方程中，一旦我们尝试从不合法的状态 f[k][j-1]f[k][j−1] 进行转移，那么 \max(\cdots)max(⋯) 将会是一个很大的数，就不会对最外层的 \min\{\cdots\}min{⋯} 产生任何影响。

此外，我们还需要将 f[0][0]f[0][0] 的值初始化为 00。在上述的状态转移方程中，当 j=1j=1 时，唯一的可能性就是前 ii 个数被分成了一段。如果枚举的 k=0k=0，那么就代表着这种情况；如果 k \neq 0k

​
 =0，对应的状态 f[k][0]f[k][0] 是一个不合法的状态，无法进行转移。因此我们需要令 f[0][0] = 0f[0][0]=0。

最终的答案即为 f[n][m]f[n][m]。

        """
        n = len(nums)
        pre = [0] + nums
        for i in range(1, n + 1):
            pre[i] += pre[i - 1]

        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = pre[i]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], pre[i] - pre[k]))
        return dp[-1][-1]


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(Solution().splitArray(nums, m))

