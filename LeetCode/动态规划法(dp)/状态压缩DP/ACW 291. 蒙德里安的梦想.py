"""
ACW 291.蒙德里安的梦想
求把N*M的棋盘分割成若干个1*2的的长方形，有多少种方案。

例如当N=2，M=4时，共有5种方案。当N=2，M=3时，共有3种方案。

如下图所示：

2411_1.jpg

输入格式
输入包含多组测试用例。

每组测试用例占一行，包含两个整数N和M。

当输入用例N=0，M=0时，表示输入终止，且该用例无需处理。

输出格式
每个测试用例输出一个结果，每个结果占一行。

数据范围
1≤N,M≤11
输入样例：
1 2
1 3
1 4
2 2
2 3
2 4
2 11
4 11
0 0
输出样例：
1
0
1
2
3
5
144
51205
"""
N = 12
cnt = [False] * (1 << N)
dp = [[0] * (1 << N) for _ in range(N)]
n, m = map(int, input().split())
while n or m:
    for i in range(N):
        for j in range(1 << N):
            dp[i][j] = 0

    dp[0][0] = 1
    for i in range(1 << n):
        cnt[i] = False
        count = 0
        for j in range(n):
            if i >> j & 1:
                # 前面连续0的个数为奇数
                if count & 1:
                    break
                count = 0
            else:
                count += 1
        if count & 1 == 0:
            cnt[i] = True

    dp[0][0] = 1
    for i in range(1, m + 1):
        for j in range(1 << n):
            for k in range(1 << n):
                # 如果当前列和前一列没有交集，并且当前行连续0的个数为偶数
                if j & k == 0 and cnt[j | k]:
                    dp[i][j] += dp[i - 1][k]

    print(dp[m][0])
    n, m = map(int, input().split())