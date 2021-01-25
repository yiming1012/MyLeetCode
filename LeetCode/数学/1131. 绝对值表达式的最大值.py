"""
1131. 绝对值表达式的最大值
给你两个长度相等的整数数组，返回下面表达式的最大值：

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

其中下标 i，j 满足 0 <= i, j < arr1.length。

 

示例 1：

输入：arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
输出：13
示例 2：

输入：arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
输出：20
 

提示：

2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-of-absolute-value-expression
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxAbsValExpr(self, arr1, arr2):
        A, B, C, D = [], [], [], []
        for i in range(len(arr1)):
            x, y = arr1[i], arr2[i]
            A.append(x + y + i)
            B.append(x + y - i)
            C.append(x - y + i)
            D.append(x - y - i)

        a = max(A) - min(A)
        b = max(B) - min(B)
        c = max(C) - min(C)
        d = max(D) - min(D)
        return max(a, b, c, d)
