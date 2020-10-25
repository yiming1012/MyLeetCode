"""
给定一张 n 个点的带权无向图，点从 0~n-1 标号，求起点 0 到终点 n-1 的最短Hamilton路径。 Hamilton路径的定义是从 0 到 n-1 不重不漏地经过每个点恰好一次。

输入格式
第一行输入整数n。

接下来n行每行n个整数，其中第i行第j个整数表示点i到j的距离（记为a[i,j]）。

对于任意的x,y,z，数据保证 a[x,x]=0，a[x,y]=a[y,x] 并且 a[x,y]+a[y,z]>=a[x,z]。

输出格式
输出一个整数，表示最短Hamilton路径的长度。

数据范围
1≤n≤20
0≤a[i,j]≤107
输入样例：
5
0 2 4 5 1
2 0 6 5 3
4 6 0 8 3
5 5 8 0 5
1 3 3 5 0
输出样例：
18
"""
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
# print(arr)

dp = [[float('inf')] * n for _ in range(1 << n)]
dp[1][0] = 0

for i in range(1, 1 << n):
    for j in range(n):
        # 本层以j位置
        if i & (1 << j):
            # 上一层结尾位置k
            for k in range(n):
                if (1 << k) & i:
                    dp[i][j] = min(dp[i][j], dp[i ^ (1 << j)][k] + arr[k][j])
print(dp[-1][-1])
