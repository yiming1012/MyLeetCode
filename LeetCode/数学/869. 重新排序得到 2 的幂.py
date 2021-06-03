"""
869. 重新排序得到 2 的幂
给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

 

示例 1：

输入：1
输出：true
示例 2：

输入：10
输出：false
示例 3：

输入：16
输出：true
示例 4：

输入：24
输出：false
示例 5：

输入：46
输出：true
 

提示：

1 <= N <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reordered-power-of-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter


class Solution:
    def reorderedPowerOf21(self, n: int) -> bool:
        # lowbit判断是否为2的幂
        def check(A):
            x = 0
            for a in A:
                x = x * 10 + int(a)
            return x & (x - 1) == 0

        arr = list(str(n))
        # 排序
        arr.sort()
        n = len(arr)
        visited = set()

        # 计算全排列
        def permutations(nums):
            if len(nums) == n and check(nums):
                return True

            for i, num in enumerate(arr):
                # 首项不为0
                if not nums and arr[i] == '0': continue
                # 去重
                if i > 0 and arr[i] == arr[i - 1] and i - 1 not in visited: continue
                if i not in visited:
                    visited.add(i)
                    if permutations(nums + [arr[i]]):
                        return True
                    visited.remove(i)
            return False

        return permutations([])

    def reorderedPowerOf22(self, n: int) -> bool:
        # 正难则反
        cnt = Counter(str(n))
        for i in range(32):
            x = 1 << i
            if Counter(str(x)) == cnt:
                return True
        return False

