"""
1073. 负二进制数相加
给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。

数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。数组形式 的数字也同样不含前导零：以 arr 为例，这意味着要么 arr == [0]，要么 arr[0] == 1。

返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。



示例：

输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
输出：[1,0,0,0,0]
解释：arr1 表示 11，arr2 表示 5，输出表示 16 。


提示：

1 <= arr1.length <= 1000
1 <= arr2.length <= 1000
arr1 和 arr2 都不含前导零
arr1[i] 为 0 或 1
arr2[i] 为 0 或 1
"""
from typing import List


class Solution:
    def addNegabinary1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a, b = 0, 0
        for a1 in arr1:
            a = a * -2 + a1

        for a2 in arr2:
            b = b * -2 + a2

        a += b
        if a == 0:
            return [0]
        res = []
        while a:
            a, k = -(a >> 1), a % 2
            res.append(k)
        return res[::-1]

    def addNegabinary2(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 11 +1 =0
        # 1 + 1 =110
        m, n = len(arr1), len(arr2)
        if m > n:
            arr1, arr2 = arr2, arr1
            m, n = n, m
        arr1 = [0] * (n - m) + arr1
        # print(arr1, arr2)
        i = n - 1
        carry = 0
        res = []
        while i >= 0:
            cursum = arr1[i] + arr2[i] + carry
            if cursum > 1:
                carry = -1
                cursum -= 2
            elif cursum < 0:
                cursum += 2
                carry = 1
            else:
                carry = 0
            res.append(cursum)
            i -= 1
        if carry:
            res.extend([1, 1])
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]


if __name__ == '__main__':
    arr1 = [1]
    arr2 = [1, 0, 1]
    print(Solution().addNegabinary1(arr1, arr2))
    print(Solution().addNegabinary2(arr1, arr2))
