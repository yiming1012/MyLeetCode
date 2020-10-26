"""
ACW 4. 多重背包问题 I
有 N 种物品和一个容量是 V 的背包。

第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤100
0<vi,wi,si≤100
输入样例
4 5
1 2 3
2 4 1
3 4 3
4 5 2
输出样例：
10
"""

# 方法一：
N, V = map(int, input().split())
arr = []
for i in range(N):
    v, w, s = map(int, input().split())
    arr.append((v, w, s))

# print(arr)
dp = [0] * (V + 1)
for v, w, s in arr:
    for j in range(V, v - 1, -1):
        for k in range(s + 1):
            if j >= k * v:
                dp[j] = max(dp[j], dp[j - k * v] + k * w)

print(dp[-1])

#方法二
N, V = map(int, input().split())
arr = []
for i in range(N):
    v, w, s = map(int, input().split())
    arr.extend([[v, w] for _ in range(s)])

# print(arr)
dp = [0] * (V + 1)
for v, w in arr:
    for j in range(V, v - 1, -1):
        dp[j] = max(dp[j], dp[j - v] + w)
print(dp[-1])

