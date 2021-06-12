"""
面试题 16.06. 最小差
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

 

示例：

输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出：3，即数值对(11, 8)
 

提示：

1 <= a.length, b.length <= 100000
-2147483648 <= a[i], b[i] <= 2147483647
正确结果在区间 [0, 2147483647] 内

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-difference-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        """
        思路：双指针
        1. 先对两个数组排序
        2. 再利用双指针交替计算最小值
        @param a:
        @param b:
        @return:
        """
        a.sort()
        b.sort()
        m, n = len(a), len(b)
        res = float('inf')
        i, j = 0, 0
        while i < m and j < n:
            res = min(res, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res


if __name__ == '__main__':
    a = [1, 3, 15, 11, 2]
    b = [23, 127, 235, 19, 8]
    print(Solution().smallestDifference(a, b))
