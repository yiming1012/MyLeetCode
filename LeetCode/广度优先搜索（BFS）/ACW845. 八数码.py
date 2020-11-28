"""
ACW845. 八数码
在一个3×3的网格中，1~8这8个数字和一个“x”恰好不重不漏地分布在这3×3的网格中。

例如：

1 2 3
x 4 6
7 5 8
在游戏过程中，可以把“x”与其上、下、左、右四个方向之一的数字交换（如果存在）。

我们的目的是通过交换，使得网格变为如下排列（称为正确排列）：

1 2 3
4 5 6
7 8 x
例如，示例中图形就可以通过让“x”先后与右、下、右三个方向的数字交换成功得到正确排列。

交换过程如下：

1 2 3   1 2 3   1 2 3   1 2 3
x 4 6   4 x 6   4 5 6   4 5 6
7 5 8   7 5 8   7 x 8   7 8 x
现在，给你一个初始网格，请你求出得到正确排列至少需要进行多少次交换。

输入格式
输入占一行，将3×3的初始网格描绘出来。

例如，如果初始网格如下所示：
1 2 3

x 4 6

7 5 8

则输入为：1 2 3 x 4 6 7 5 8

输出格式
输出占一行，包含一个整数，表示最少交换次数。

如果不存在解决方案，则输出”-1”。

输入样例：
2  3  4  1  5  x  7  6  8
输出样例
19
"""
# 数字华容道
import collections

target = ['1', '2', '3', '4', '5', '6', '7', '8', 'x']
pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
start = list(map(str, input().split()))
queue = collections.deque()
queue.append((start, 0))
visited = set()
visited.add(tuple(start))

flag = False

while queue:
    cur, step = queue.popleft()
    if cur == target:
        print(step)
        flag = True
        break
    index = cur.index("x")
    x = index // 3
    y = index % 3
    for i, j in pos:
        tmp = cur.copy()
        if 0 <= x + i < 3 and 0 <= y + j < 3:
            nex = (x + i) * 3 + (y + j)
            tmp[nex], tmp[index] = tmp[index], tmp[nex]
            if tuple(tmp) not in visited:
                queue.append((tmp, step + 1))
                visited.add(tuple(tmp))

if not flag:
    print(-1)
