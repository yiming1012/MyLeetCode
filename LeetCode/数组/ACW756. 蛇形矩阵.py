"""
ACW756. 蛇形矩阵
输入两个整数n和m，输出一个n行m列的矩阵，将数字 1 到 n*m 按照回字蛇形填充至矩阵中。

具体矩阵形式可参考样例。

输入格式
输入共一行，包含两个整数n和m。

输出格式
输出满足要求的矩阵。

矩阵占n行，每行包含m个空格隔开的整数。

数据范围
1≤n,m≤100
输入样例：
3 3
输出样例：
1 2 3
8 9 4
7 6 5
"""
n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
pos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 1
a, b = 0, 0
for i in range(1, n * m + 1):
    graph[a][b] = i
    x = a + pos[d][0]
    y = b + pos[d][1]
    if x < 0 or x >= n or y < 0 or y >= m or graph[x][y]:
        d = (d + 1) % 4
        x = a + pos[d][0]
        y = b + pos[d][1]
    a, b = x, y

for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()
