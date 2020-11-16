"""
240. 食物链
动物王国中有三类动物A,B,C，这三类动物的食物链构成了有趣的环形。

A吃B， B吃C，C吃A。

现有N个动物，以1－N编号。

每个动物都是A,B,C中的一种，但是我们并不知道它到底是哪一种。

有人用两种说法对这N个动物所构成的食物链关系进行描述：

第一种说法是”1 X Y”，表示X和Y是同类。

第二种说法是”2 X Y”，表示X吃Y。

此人对N个动物，用上述两种说法，一句接一句地说出K句话，这K句话有的是真的，有的是假的。

当一句话满足下列三条之一时，这句话就是假话，否则就是真话。

1） 当前的话与前面的某些真的话冲突，就是假话；
2） 当前的话中X或Y比N大，就是假话；
3） 当前的话表示X吃X，就是假话。

你的任务是根据给定的N和K句话，输出假话的总数。

输入格式
第一行是两个整数N和K，以一个空格分隔。

以下K行每行是三个正整数 D，X，Y，两数之间用一个空格隔开，其中D表示说法的种类。

若D=1，则表示X和Y是同类。

若D=2，则表示X吃Y。

输出格式
只有一个整数，表示假话的数目。

数据范围
1≤N≤50000,
0≤K≤100000
输入样例：
100 7
1 101 1
2 1 2
2 2 3
2 3 3
1 1 3
2 3 1
1 5 5
输出样例：
3
难度：中等
时/空限制：1s / 64MB
总通过数：5040
总尝试数：10706
来源：《算法竞赛进阶指南》, 模板题 , NOI2001
算法标签

"""
N, K = map(int, input().split())
parent = [i for i in range(N + 1)]
path = [0] * (N + 1)


def find(x):
    if x != parent[x]:
        t = find(parent[x])
        path[x] += path[parent[x]]
        parent[x] = t
    return parent[x]


res = 0
for i in range(K):
    D, X, Y = map(int, input().split())
    if X > N or Y > N:
        res += 1
        continue

    px, py = find(X), find(Y)
    if D == 1:
        if px == py and (path[X] - path[Y]) % 3:
            res += 1
        elif px != py:
            parent[px] = py
            path[px] = path[Y] - path[X]
    else:
        if px == py and (path[X] - path[Y] - 1) % 3:
            res += 1
        else:
            parent[px] = py
            path[px] = path[Y] - path[X] + 1

print(res)
