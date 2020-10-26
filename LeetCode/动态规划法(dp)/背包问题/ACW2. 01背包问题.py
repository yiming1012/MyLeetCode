"""
ACW2.01背包问题
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

第 i 件物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤1000
0<vi,wi≤1000
输入样例
4 5
1 2
2 4
3 4
4 5
输出样例：
8
难度：简单
时/空限制：1s / 64MB
总通过数：31297
总尝试数：54709
来源：背包九讲 , 模板题
算法标签
"""
# 方法一
N, V = map(int, input().split())
arr = []
for i in range(N):
    v, w = map(int, input().split())
    arr.append((v, w))
# print(arr)

dp = [[0] * (V + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(V + 1):
        dp[i][j] = dp[i - 1][j]
        v, w = arr[i - 1]
        if j >= v:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - v] + w)

print(dp[-1][-1])

# 方法二
N, V = map(int, input().split())
# print(N,V)
arr = []
for i in range(N):
    v, w = map(int, input().split())
    arr.append((v, w))
    # print(v,w)

# print(arr)
dp = [0] * (V + 1)
for v, w in arr:
    for i in range(V, v - 1, -1):
        dp[i] = max(dp[i], dp[i - v] + w)
# print(dp)
print(dp[-1])
