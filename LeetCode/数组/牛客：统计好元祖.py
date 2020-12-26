"""
牛客：统计好元祖
链接：https://ac.nowcoder.com/acm/contest/10324/B
来源：牛客网

题目描述
现在给定一个数组arr，和a,b两个数字，你要做的就是找到（i，j，k）。且满足
    1. 0 <= i < j < k < arr.size()
    2. |arr[i] - arr[j]| <= a
    3. |arr[j] - arr[k]| <= b
统计满足条件的个数并返回(最后结果可能很大，请取1000000007的余数)。
示例1
输入
复制
[7,1,8,9,0],3,3
返回值
复制
1
说明
只有（7，8，9）符合要求
备注:
arr.size() <= 5000
其余变量均<=1e9
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param arr int整型一维数组
# @param a int整型
# @param b int整型
# @return int整型
#
class Solution:
    def countTriplets(self, arr, a, b):
        # write code here
        mod = 10 ** 9 + 7
        n = len(arr)
        A = [0] * n
        B = [0] * n
        res = 0
        for i in range(1, n):
            for j in range(i):
                if abs(arr[i] - arr[j]) <= a:
                    A[i] += 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) <= b:
                    B[i] += 1
        for i in range(1, n - 1):
            res += A[i] * B[i]
        return res % mod
