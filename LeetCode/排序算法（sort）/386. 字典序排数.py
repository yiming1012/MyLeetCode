"""
386. 字典序排数
给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，

给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lexicographical-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import functools
from typing import List


class Solution:
    def lexicalOrder1(self, n: int) -> List[int]:
        return sorted(list(range(1, n + 1)), key=lambda x: str(x))

    def lexicalOrder2(self, n: int) -> List[int]:
        def mycmp(y, x):
            if x < y:
                return 1
            elif x > y:
                return -1
            else:
                return 0

        s = list(map(str, range(1, n + 1)))
        s.sort(key=functools.cmp_to_key(mycmp))
        return s

    def lexicalOrder3(self, n: int) -> List[int]:
        def dfs(num):
            if num > n: return
            res.append(num)
            for i in range(10):
                dfs(num * 10 + i)

        res = []
        for i in range(1, 10):
            dfs(i)
        return res


if __name__ == '__main__':
    n = 13
    print(Solution().lexicalOrder1(n))
    print(Solution().lexicalOrder2(n))
    print(Solution().lexicalOrder3(n))
