"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        思路：排列组合
        1. 首先将每个数的阶层存到数组中，没必要在程序执行过程中实现递归
        2.

        
        @param n:
        @param k:
        @return:
        """
        fac = [1] * (n + 1)
        for i in range(1, n + 1):
            fac[i] = fac[i - 1] * i

        arr = list(range(1, n + 1))
        res = []
        k -= 1
        for i in range(n - 1, -1, -1):
            index, k = divmod(k, fac[i])
            res.append(str(arr[index]))
            arr.pop(index)
        return "".join(res)


if __name__ == '__main__':
    n = 4
    k = 9
    s = "abc"
    print(Solution().getPermutation(n, k))
