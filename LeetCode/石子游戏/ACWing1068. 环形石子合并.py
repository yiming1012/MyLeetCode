"""
ACWing1068. 环形石子合并
将 n 堆石子绕圆形操场排放，现要将石子有序地合并成一堆。

规定每次只能选相邻的两堆合并成新的一堆，并将新的一堆的石子数记做该次合并的得分。

请编写一个程序，读入堆数 n 及每堆的石子数，并进行如下计算：

选择一种合并石子的方案，使得做 n−1 次合并得分总和最大。
选择一种合并石子的方案，使得做 n−1 次合并得分总和最小。
输入格式
第一行包含整数 n，表示共有 n 堆石子。

第二行包含 n 个整数，分别表示每堆石子的数量。

输出格式
输出共两行：

第一行为合并得分总和最小值，

第二行为合并得分总和最大值。

数据范围
1≤n≤200
输入样例：
4
4 5 9 4
输出样例：
43
54
难度：简单
时/空限制：1s / 64MB
总通过数：1274
总尝试数：1703
来源：《信息学奥赛一本通》
算法标签
DP区间DP环形区间DP

"""
n = int(input())
nums = list(map(int, input().split()))
# 环形数组一般思路：在原数组后面拼接 除去最后一位的原数组
nums = nums[:] + nums[:-1]

# 前缀和
pre = [0] * (2 * n)
for i in range(2 * n - 1):
    pre[i + 1] = pre[i] + nums[i]

# 最小值
min_dp = [[float('inf')] * (2 * n - 1) for _ in range(2 * n - 1)]
# 最大值
max_dp = [[float('-inf')] * (2 * n - 1) for _ in range(2 * n - 1)]

for i in range(2 * n - 1):
    min_dp[i][i] = 0
    max_dp[i][i] = 0

for v in range(1, n + 1):
    for l in range(2 * n - v):
        r = l + v - 1
        for k in range(l, r):
            min_dp[l][r] = min(min_dp[l][r], min_dp[l][k] + min_dp[k + 1][r] + pre[r + 1] - pre[l])
            max_dp[l][r] = max(max_dp[l][r], max_dp[l][k] + max_dp[k + 1][r] + pre[r + 1] - pre[l])

min_res, max_res = float('inf'), float('-inf')
for i in range(n):
    min_res = min(min_res, min_dp[i][i + n - 1])
    max_res = max(max_res, max_dp[i][i + n - 1])
print(min_res)
print(max_res)
