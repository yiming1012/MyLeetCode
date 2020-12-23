"""
ACW135. 最大子序和
输入一个长度为n的整数序列，从中找出一段长度不超过m的连续子序列，使得子序列中所有数的和最大。

注意： 子序列的长度至少是1。

输入格式
第一行输入两个整数n,m。

第二行输入n个数，代表长度为n的整数序列。

同一行数之间用空格隔开。

输出格式
输出一个整数，代表该序列的最大子序和。

数据范围
1≤n,m≤300000
输入样例：
6 4
1 -3 5 1 -2 3
输出样例：
7
"""
n, m = map(int, input().split())
nums = list(map(int, input().split()))
import collections

queue = collections.deque()

pre = [0] * (n + 1)
for i in range(n):
    pre[i + 1] = pre[i] + nums[i]

queue.append(0)
res = float('-inf')
for i, num in enumerate(nums):
    while queue and queue[0] < i + 1 - m:
        queue.popleft()

    res = max(res, pre[i + 1] - pre[queue[0]])
    while queue and pre[queue[-1]] >= pre[i + 1]:
        queue.pop()
    queue.append(i + 1)
print(res)
