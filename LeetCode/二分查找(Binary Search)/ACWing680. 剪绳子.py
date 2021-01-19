"""
ACWing680. 剪绳子
有N根绳子，第i根绳子长度为LiLi，现在需要M根等长的绳子，你可以对N根绳子进行任意裁剪（不能拼接），请你帮忙计算出这M根绳子最长的长度是多少。
输入格式
第一行包含2个正整数N、M，表示原始绳子的数量和需求绳子的数量。
第二行包含N个整数，其中第 i 个整数LiLi表示第 i 根绳子的长度。
输出格式
输出一个数字，表示裁剪后最长的长度，保留两位小数。
数据范围
1≤N,M≤100000
0<Li<10^9
输入样例：
3 4
3 5 4
输出样例：
2.50
样例解释
第一根和第三根分别裁剪出一根2.50长度的绳子，第二根剪成2根2.50长度的绳子，刚好4根。
"""


def check(mid):
    cnt = 0
    for x in arr:
        cnt += x // mid

    return cnt >= M


N, M = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, max(arr)

while r - l >= 1e-6:
    mid = (l + r) / 2
    if check(mid):
        l = mid
    else:
        r = mid

print("%.2f" % l)
