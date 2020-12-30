"""
1291. 顺次数
我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。

请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。

 

示例 1：

输出：low = 100, high = 300
输出：[123,234]
示例 2：

输出：low = 1000, high = 13000
输出：[1234,2345,3456,4567,5678,6789,12345]
 

提示：

10 <= low <= high <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sequential-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        思路：两层for循环遍历
        1. 时间复杂度和空间复杂度都是O(1)
        @param low:
        @param high:
        @return:
        """
        res = []
        for i in range(1, 10):
            num = 0
            for j in range(i, 10):
                num = num * 10 + j
                if low <= num <= high:
                    res.append(num)
        return sorted(res)


if __name__ == '__main__':
    low, high = 100, 300
    print(Solution().sequentialDigits(low, high))
