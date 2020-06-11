"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        思路：每次和栈顶数组对比
        """
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            arr = res[-1].copy()
            arr.insert(0, 0)
            arr.append(0)
            aa = []
            for j in range(len(arr) - 1):
                aa.append(arr[j] + arr[j + 1])
            res.append(aa)
        return res


    def generate2(self, numRows: int) -> List[List[int]]:
        """
        思路：每次和栈顶数组对比
        """
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            arr = res[-1]
            aa = [1]
            for j in range(len(arr) - 1):
                aa.append(arr[j] + arr[j + 1])
            aa.append(1)
            res.append(aa)
        return res

    def generate3(self, numRows: int) -> List[List[int]]:
        """
        简便方法
        """
        res = [[1] * l for l in range(1, numRows + 1)]
        print(res)
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res


if __name__ == '__main__':
    numRows = 5
    print(Solution().generate(numRows))
    print(Solution().generate2(numRows))
    print(Solution().generate3(numRows))
