"""
1215. 步进数
如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是 1，那么这个数就是一个「步进数」。

例如，321 是一个步进数，而 421 不是。

给你两个整数，low 和 high，请你找出在 [low, high] 范围内的所有步进数，并返回 排序后 的结果。

 

示例：

输入：low = 0, high = 21
输出：[0,1,2,3,4,5,6,7,8,9,10,12,21]
 

提示：

0 <= low <= high <= 2 * 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stepping-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        arr = list(range(10))
        queue = collections.deque(arr)
        res = []
        visited = set(arr)
        while queue:
            num = queue.popleft()
            if low <= num <= high:
                res.append(num)
            mod = num % 10
            if mod + 1 <= 9 and num * 10 + mod + 1 <= high and num * 10 + mod + 1 not in visited:
                queue.append(num * 10 + mod + 1)
            if mod - 1 >= 0 and num * 10 + mod - 1 <= high and num * 10 + mod - 1 not in visited:
                queue.append(num * 10 + mod - 1)
        return sorted(res)


if __name__ == '__main__':
    low = 0
    high = 21
    print(Solution().countSteppingNumbers(low, high))
