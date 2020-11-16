"""
837. 连通块中点的数量

给定一个包含n个点（编号为1~n）的无向图，初始时图中没有边。

现在要进行m个操作，操作共有三种：

“C a b”，在点a和点b之间连一条边，a和b可能相等；
“Q1 a b”，询问点a和点b是否在同一个连通块中，a和b可能相等；
“Q2 a”，询问点a所在连通块中点的数量；
输入格式
第一行输入整数n和m。

接下来m行，每行包含一个操作指令，指令为“C a b”，“Q1 a b”或“Q2 a”中的一种。

输出格式
对于每个询问指令”Q1 a b”，如果a和b在同一个连通块中，则输出“Yes”，否则输出“No”。

对于每个询问指令“Q2 a”，输出一个整数表示点a所在连通块中点的数量

每个结果占一行。

数据范围
1≤n,m≤105
输入样例：
5 5
C 1 2
Q1 1 2
Q2 1
C 2 5
Q2 5
输出样例：
Yes
2
3
"""
n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
cnt = [1] * (n + 1)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


for i in range(m):
    arr = input().split()
    if arr[0] == "C":
        x, y = find(int(arr[1])), find(int(arr[2]))
        if x != y:
            parent[y] = x
            cnt[x] += cnt[y]
    elif arr[0] == "Q1":
        if find(int(arr[1])) == find(int(arr[2])):
            print("Yes")
        else:
            print("No")
    else:
        x = find(int(arr[1]))
        print(cnt[x])
